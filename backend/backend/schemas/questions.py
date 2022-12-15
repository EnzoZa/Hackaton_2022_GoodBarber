from typing import List, Optional
from pydantic import BaseModel

class Question(BaseModel):
    """Question modele."""
    id: int
    question: str
    response: Optional[str]

class QuestionsResponse(BaseModel):
    """Question Response modele."""
    data: List[Question]