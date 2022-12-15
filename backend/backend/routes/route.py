from fastapi import APIRouter, status, Depends
from typing import List
from schemas.categories import Categorie
from schemas.questions import QuestionsResponse
from services.Questions import QuestionService


# router
router: APIRouter = APIRouter(prefix="")

@router.get("/questions", status_code=status.HTTP_200_OK)
def get_questions(
    service: QuestionService = Depends(QuestionService)
) -> QuestionsResponse:
    """Return questions to client."""
    result = service.get_questions()
    return QuestionsResponse(data=result)

@router.post("/questions/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def submit_question(
    questions: QuestionsResponse,
    service: QuestionService = Depends(QuestionService)
) -> None:
    """"""
    await service.post_questions(questions)

@router.get("/categories", status_code=status.HTTP_200_OK)
def get_categories() -> List[Categorie]:
    """Return all categories."""
    categories: List[Categorie] = [
        Categorie(id = 1,name = "Sport"),
        Categorie(id = 2,name = "Fete"),
        Categorie(id = 3,name = "Informatique")
    ]
    return categories
