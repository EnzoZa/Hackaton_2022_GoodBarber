from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import List

class Categorie(BaseModel):
    """Categorie model."""
    id: int
    name: str
