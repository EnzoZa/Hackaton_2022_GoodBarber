from pydantic import BaseModel, Field

class Articles(BaseModel):
    """Articles Model."""
    title: str
    company_name: str = Field(alias="companyName")
    description: str
    articles: str
