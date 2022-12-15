import openai
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