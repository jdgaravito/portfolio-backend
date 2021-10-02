import fastapi
from typing import Optional, Text
from fastapi.params import Depends
from app.models.portfolio_model import Project
router = fastapi.APIRouter()

@router.get('/portfolio')
async def portfolio_index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    """Only get 10 publushed projects""" 
    if published: 
        return {'data': f'Portfolio list showing {limit} projects'}
    else:
        return {'data': f'{limit} projects from db'} 