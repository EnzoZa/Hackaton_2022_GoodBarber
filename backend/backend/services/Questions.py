from typing import List
from schemas.questions import Question, QuestionsResponse

class QuestionService:
    """QuestionService."""
    def get_questions(self) -> List[Question]:
        """Method to get questions list of base questions."""
        questions: List[int, str] = [
            {"id":1, "question": "Question 1"},
            {"id":2, "question": "Question 2"}
        ]
        return list(map(Question.parse_obj, questions))

    def post_questions(self, questions: QuestionsResponse) -> None:
        """Treat response of questions."""
        pass