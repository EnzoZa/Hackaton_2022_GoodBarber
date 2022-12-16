from ast import Dict
from typing import List
from schemas.articles import Articles
from services.openai import OpenAIService
from schemas.questions import Question, QuestionsResponse
from pexels_api import API as pexelsApi
from bs4 import BeautifulSoup
import os


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
        # Instanciate pexelsApi
        PEXELS_API_KEY = '563492ad6f917000010000017678ae0d46924806bf5c88bffee69782'
        api = pexelsApi(PEXELS_API_KEY)

        search = f"{keyword} {category} {website_category}"

        # search main photo
        api.search(search, page=1, results_per_page=1)
        logo = api.get_entries()

        api.search(search, page=1, results_per_page=10)
        photos = api.get_entries()
        photo_to_diplay = [photo.url for photo in photos]

        soup = BeautifulSoup(articles.articles, 'html.parser')
        h1s = soup.find_all('h1')
        print(h1s)
        # Pour chaque élément div, ajouter une image avant l'élément
        for i, h1 in enumerate(h1s):
            # Créer un élément img avec l'URL de l'image à ajouter
            try:
                img_tag = soup.new_tag("img", src=photo_to_diplay[i], alt="Image")
                print("*"*50)
                print(img_tag)
                print(type(h1))
                h1.insert_before(img_tag)
            except:
                pass
        
        articles.articles = soup.prettify()
        path = os.path.abspath(os.path.dirname(__file__))

        # Write a new html file parsed
        with open(f"{path}/template/index.html", "r+") as f:
            lines = f.read()

        lines = lines.replace("{{titleName}}", articles.title)
        lines = lines.replace("{{logo}}", logo.url)
        lines = lines.replace("{{brandName}}", articles.company_name)
        lines = lines.replace("{{titleSection}}", articles.title)
        lines = lines.replace("{{introducingProposal}}", articles.description)
        lines = lines.replace("{{descriptionProposal}}", articles.description)
        lines = lines.replace("{{articles}}", articles.articles)

        print("*"*100)
        print(articles.articles)
        print("*"*100)

        with open(f"{path}/template/template.html", "w") as f:
            f.write(lines)
