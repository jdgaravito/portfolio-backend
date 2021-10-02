from sqlmodel import SQLModel, Field
from typing import Optional


class ProjectBase(SQLModel):
    name: str
    artist: str
    award: Optional[str] = None



class Project(ProjectBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ProjectCreate(ProjectBase):
    pass