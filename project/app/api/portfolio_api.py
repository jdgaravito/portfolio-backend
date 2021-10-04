import fastapi
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List

from app.db import get_session
from app.models.portfolio_model import Project


router = fastapi.APIRouter()

@router.get('/portfolio', response_model=List[Project],
status_code=status.HTTP_200_OK)
async def get_all_projects(session: AsyncSession = Depends(get_session)):
    statement=select(Project)
    result= await session.execute(statement)
    projects = result.scalars().all()

    # return [Project(name=project.name, 
    #                 summary=project.summary,
    #                 description=project.description,
    #                 category=project.category,
    #                 award=project.award,
    #                 url=project.url,
    #                 published=project.published,
    #                 image=project.image,
    #                 images=project.images,
    #                 learning=project.learning,
    #                 tech=project.tech,
    #                 tools=project.tools) 
    #         for project in projects]
    return projects


@router.post('/portfolio', response_model=Project, status_code=status.HTTP_201_CREATED)
async def add_project(project: Project, session: AsyncSession = Depends(get_session)):
    project = Project(name=project.name, 
                    summary=project.summary,
                    description=project.description,
                    category=project.category,
                    award=project.award,
                    url=project.url,
                    published=project.published,
                    image=project.image,
                    images=project.images,
                    learning=project.learning,
                    tech=project.tech,
                    tools=project.tools)  
    session.add(project)
    await session.commit()
    await session.refresh(project)
    return project

@router.get('/portfolio/{project_id}', response_model=Project)
async def get_a_project(project_id: int, session: AsyncSession= Depends(get_session)):
    statement = select(Project).where(Project.id == project_id)
    result = await session.execute(statement)
    if None == result:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND) 
   
    return result