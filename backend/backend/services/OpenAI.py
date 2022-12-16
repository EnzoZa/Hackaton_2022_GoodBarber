from typing import Dict
import openai
import json
from schemas.articles import Articles

class OpenAIService:
    """OpenAI Service."""

    def __init__(self):
        openai.api_key="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"

    def get_categorie_proposal(self , keyword: str):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Voici une liste de thème dis moi de quelle thème se rapproche le plus ce mot (même si c'est le thème en question) :
            Thème : Sport, Évènementiel, Écologie, Informatique, Vêtement, Automobile, Blog, Personnel, Religion, Touristique, Cours, Créateur de contenu, Vente, Association, Restaurant, Radio, Épicerie
            Par exemple : Vente : Vente, Musculation : Sport, Fête : Évènementiel, Arbre : Écologie, Portfolio : Personnel, Chrétien : Religion, Éducatif : Cours.
            Mais Sport ne donne pas Musculation, il redonne Sport : Sport : Sport. Pareil avec tout les autres thèmes
            {keyword} : """,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].text

    def get_type_proposal(self , word):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Voici une liste de thème dis moi de quelle thème se rapproche le plus ce mot (même si c'est le thème en question) :
            Thème : E-Commerce, Blog, Site Vitrine, Coaching
            Par exemple : E-Commerce: E-Commerce, Portfolio: Site Vitrine, Formation: Coaching, Vente: E-Commerce, Forum : E-Commerce.
            Mais Site Vitrine ne donne pas Portfolio, il redonne Site Vitrine: Site Vitrine. Pareil avec tout les autres thèmes
            {word} : """,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].text

    def get_article_proposal(self , category: str, website_category: str, keyword: str, country: str = "France") -> Articles:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
            Génère toute mes instructions suivante dans un json :
            Génère moi un titre en rapport avec le '{keyword}' '{category}' qui intéresserai une personne vivant en {country} en 2022 pour un site de '{website_category}'.
            Génère moi un nom d'entreprise en rapport avec le '{keyword}' '{category}' qui intéresserai une personne vivant en {country} en 2022 pour un site de '{website_category}'.
            Génère moi une description complète en rapport avec le '{keyword}' '{category}' qui intéresserai une personne vivant en {country} en 2022 pour un site de '{website_category}'.
            Maintenant Génère mon instruction dans clé articles en un seul champ String :
            Génère moi aussi 10 articles avec titre et description en html en rapport avec le '{keyword}' '{category}' qui intéresserai une personne vivant en {country} en 2022 pour un site de '{website_category}'.""",
            temperature=0,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        articles = json.loads(response.choices[0].text)
        print(articles)
        return Articles.parse_obj(articles)
