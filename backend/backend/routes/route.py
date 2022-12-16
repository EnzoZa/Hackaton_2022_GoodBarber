from fastapi import APIRouter, status, Depends
from fastapi.responses import HTMLResponse, FileResponse
from typing import List
from schemas.categories import Categorie
from schemas.questions import QuestionsResponse
from services.questions import QuestionService
import os

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
def submit_question(
    questions: QuestionsResponse,
    service: QuestionService = Depends(QuestionService)
) -> None:
    """"""
    service.post_questions(questions)

@router.get("/categories", status_code=status.HTTP_200_OK)
def get_categories() -> List[Categorie]:
    """Return all categories."""
    categories: List[Categorie] = [
        Categorie(id = 1,name = "Sport"),
        Categorie(id = 2,name = "Fete"),
        Categorie(id = 3,name = "Informatique")
    ]
    return categories

@router.get("/files/{folder}/{subpath}", response_class=FileResponse)
@router.get("/files/{subpath}", response_class=FileResponse)
def iframe( subpath: str, folder: str= None):
    if folder:
        subpath = f"{folder}/{subpath}"
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return f"{path}/services/template/{subpath}"