from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class GitHubRepoResponse(BaseModel):
    """Schema para respuesta de repositorio de GitHub"""
    id: int
    repo_id: int
    name: str
    full_name: str
    description: Optional[str] = None
    html_url: str
    homepage: Optional[str] = None
    language: Optional[str] = None
    stargazers_count: int
    forks_count: int
    topics: Optional[List[str]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    pushed_at: Optional[str] = None
    cached_at: datetime
    
    class Config:
        from_attributes = True