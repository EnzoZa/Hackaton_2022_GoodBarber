import openai
from pexels_api import API
from bs4 import BeautifulSoup

class OpenAIService:
    """OpenAI Service."""

    def __init__(self):
        openai.api_key="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"

    async def get_categorie_proposal(self , keyword):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Voici une liste de thème dis moi de quelle thème se rapproche le plus ce mot (même si c'est le thème en question) :
            Thème : Sport, Évènementiel, Écologie, Informatique, Vêtement, Touriste, Blog, Personnel, Religion, Touristique, Cours, Créateur de contenu, Vente, Association, Restaurant, Radio, Épicerie
            Par exemple : Vente : Vente, Musculation : Sport, Fête : Évènementiel, Arbre : Écologie, Portfolio : Personnel, Chrétien : Religion, Éducatif : Cours.
            Mais Sport ne donne pas Musculation, il redonne Sport : Sport : Sport. Pareil avec tout les autres thèmes
            {keyword.capitalize()} : """,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].text

    async def get_type_proposal(self , word):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Voici une liste de thème dis moi de quelle thème se rapproche le plus ce mot (même si c'est le thème en question) :
            Thème : E-Commerce, Blog, Site Vitrine, Coaching
            Par exemple : E-Commerce: E-Commerce, Portfolio: Site Vitrine, Formation: Coaching, Vente: E-Commerce, Forum : E-Commerce.
            Mais Site Vitrine ne donne pas Portfolio, il redonne Site Vitrine: Site Vitrine. Pareil avec tout les autres thèmes
            {word.capitalize()} : """,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].text

    async def get_type_proposal(self , word):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Voici une liste de thème dis moi de quelle thème se rapproche le plus ce mot (même si c'est le thème en question) :
            Thème : E-Commerce, Blog, Site Vitrine, Coaching
            Par exemple : E-Commerce: E-Commerce, Portfolio: Site Vitrine, Formation: Coaching, Vente: E-Commerce, Forum : E-Commerce.
            Mais Site Vitrine ne donne pas Portfolio, il redonne Site Vitrine: Site Vitrine. Pareil avec tout les autres thèmes
            {word.capitalize()} : """,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].text

    async def get_article_proposal(self , theme, type, keyword, country):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Génère toute mes instructions suivante dans un json :
            Génère moi un titre en rapport avec le '{keyword.capitalize()}' '{theme.capitalize()}' qui intéresserai une personne vivant en {country.capitalize()} en 2022 pour un site de '{type.capitalize()}'.
            Génère moi un nom d'entreprise en rapport avec le '{keyword.capitalize()}' '{theme.capitalize()}' qui intéresserai une personne vivant {country.capitalize()} en en 2022 pour un site de '{type.capitalize()}'.
            Génère moi une description complète en rapport avec le '{keyword.capitalize()}' '{theme.capitalize()}' qui intéresserai une personne vivant {country.capitalize()} en en 2022 pour un site de '{type.capitalize()}'.
            Maintenant Génère mon instruction dans clé articles en un seul champ String : 
            Génère moi aussi 10 articles avec titre et description en html en rapport avec le '{keyword.capitalize()}' '{theme.capitalize()}' qui intéresserai une personne vivant {country.capitalize()} en 2022 pour un site de '{type.capitalize()}'.""",
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].text

    async def get_website_proposal(self , keyword, theme, type, country) :
        # Type your Pexels API
        PEXELS_API_KEY = '563492ad6f917000010000017678ae0d46924806bf5c88bffee69782'
        # Create API object
        api = API(PEXELS_API_KEY)
        search = {keyword.capitalize()} + ' ' + {theme.capitalize()} + ' ' + {type.capitalize()}
        api.search(search, page=1, results_per_page=1) 
        photo = api.get_entries()

        with open("template/index.html", "r+") as f:
            # lire le contenu du fichier
            contenu = f.read()

            # modifier le contenu du fichier
            #Inclure la photo photo.url 
            contenu = contenu.replace("TitleName", "nouveau texte") # get_article_proposal['title']
            contenu = contenu.replace("BrandName", "nouveau texte") # get_article_proposal['companyName']
            contenu = contenu.replace("TitleSection", "nouveau texte") # get_article_proposal['title']
            contenu = contenu.replace("IntroducingProposal", "nouveau texte") # get_article_proposal['description']
            contenu = contenu.replace("DescriptionProposal", "nouveau texte") # get_article_proposal['description']
            contenu = contenu.replace("<!-- ARTICLES -->", "nouveau texte") # get_article_proposal['articles']
            # écrire les modifications dans le fichier
            f.write(contenu)
        
        # Search 10 photo for the articles
        search = {keyword.capitalize()} + ' ' + {theme.capitalize()} + ' ' + {type.capitalize()} + ' ' + {country.capitalize()}
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