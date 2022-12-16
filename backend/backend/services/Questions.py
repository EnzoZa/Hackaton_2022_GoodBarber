from ast import Dict
from typing import List
from schemas.articles import Articles
from services.openai import OpenAIService
from schemas.questions import Question, QuestionsResponse
from pexels_api import API as pexelsApi
import shutil
from bs4 import BeautifulSoup
import os
import fileinput


class QuestionService:
    """QuestionService."""

    def get_questions(self) -> List[Question]:
        """Method to get questions list of base questions."""
        questions: List[int, str] = [
            {"id":1, "question": "Donnez un mot clé pour décrire votre besoin ?"},
            {"id":2, "question": "Quelle type de site web souhaitez vous avoir ?"}
        ]
        return list(map(Question.parse_obj, questions))

    def post_questions(self, questions: QuestionsResponse) -> None:
        """Treat response of questions."""
        ai = OpenAIService()

        keyword: str = questions.data[0].response
        category: str = ai.get_categorie_proposal(questions.data[0].response.capitalize())
        website_category: str = ai.get_type_proposal(questions.data[1].response.capitalize())
        articles: Articles = ai.get_article_proposal(keyword=keyword, category=category, website_category=website_category)

        # Generation of template
        self._build_template(keyword=keyword, category=category, website_category=website_category, articles=articles)

    def _build_template(self, keyword: str, category: str, website_category: str, articles: Articles,  country: str= "France"):
        # Type your Pexels API
        PEXELS_API_KEY = '563492ad6f917000010000017678ae0d46924806bf5c88bffee69782'
        # Create API object
        api = pexelsApi(PEXELS_API_KEY)
        search = f"{keyword} {category} {website_category}"
        api.search(search, page=1, results_per_page=1)
        photo = api.get_entries()

        # shutil.copytree("backend/services/template/index.html", "backend/services/template/index_proposal.html")
        file_path: str = "/Users/a1201/Desktop/Hackaton_2022_GoodBarber/backend/backend/services/template/index.html"

        template_file = open(file_path, 'r')
        Lines = template_file.readlines()
        print(Lines)
        # with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        #     for line in file:
        #         print(line)
                # line.replace("{{titleName}}", articles.title)
                # line.replace("{{brandName}}", articles.company_name)
                # line.replace("{{titleSection}}", articles.title)
                # line.replace("{{introducingProposal}}", articles.description)
                # line.replace("{{descriptionProposal}}", articles.description)
                # line.replace("{{articles}}", articles.articles)


        return

        # Search 10 photo for the articles"
        search = f"{keyword} {category} {website_category} {country}"
        api.search(search, page=1, results_per_page=10)
        # Get photo entries
        photos = api.get_entries()
        diplay_photos = []
        # Loop the five photos
        for photo in photos:
            # Print photographer
            print('Photographer: ', photo.photographer)
            # Print url
            print('Photo url: ', photo.url)
            diplay_photos.append(photo.url)
            # Print original size url
            print('Photo original size: ', photo.original)

        # Créer un objet BeautifulSoup à partir de la chaîne de caractères HTML
        soup = BeautifulSoup(f, 'html.parser')

        # Récupérer tous les éléments div de la page
        div = soup.find('div', class_='articles')
        h1s = div.find_all('h1')
        # Pour chaque élément div, ajouter une image avant l'élément
        for i in range (0, len(h1s)):
            # Créer un élément img avec l'URL de l'image à ajouter
            img_tag = soup.new_tag("img", src=diplay_photos[i], alt="Image")

            # Insérer l'élément img avant l'élément div
            # h1.insert_before(img_tag)
            h1s[i].insert_before(img_tag)

        # Afficher le contenu HTML modifié
        print(soup.prettify())
        return soup.prettify()