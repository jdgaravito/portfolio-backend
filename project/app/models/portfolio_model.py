from datetime import datetime
from typing import List, Optional
from sqlmodel import SQLModel, Field


class ProjectBase(SQLModel):
    name: str
    summary: str
    description: str
    tags: Optional[List[str]] = ["Project with love"]
    award: Optional[str] = None
    url: Optional[str] = None
    published: datetime = datetime.utcnow()
    image: str = "placeholderMainImage"
    images: List[str] = ["placeholderImage1", "placeholderImage2", "placeholderImage3", "placeholderImage4"]
    learning: Optional[str]
    tech: Optional[str]
    tools: Optional[str]



class Project(ProjectBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ProjectCreate(ProjectBase):
    pass