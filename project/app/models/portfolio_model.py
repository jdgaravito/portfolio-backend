from datetime import datetime
from typing import List, Optional, Set
from sqlmodel import SQLModel, Field


class ProjectBase(SQLModel):
    name: Optional[str]
    summary: Optional[str]
    description: Optional[str]
    category: Set[str] = set()
    award: Optional[str] = None
    url: Optional[str] = None
    published: datetime = datetime.utcnow()
    image: str = "placeholderMainImage"
    images: List[str] = []
    learning: Optional[str]
    tech: Optional[str]
    tools: Optional[str]



class Project(ProjectBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ProjectCreate(ProjectBase):
    pass