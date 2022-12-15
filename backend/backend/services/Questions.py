from typing import List
from services.openai import OpenAIService
from schemas.questions import Question, QuestionsResponse

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

        category = ai.get_categorie_proposal(questions.data[0].response)
        website_category = ai.get_type_proposal(questions.data[1].response)

        print(category)
        print(website_category)