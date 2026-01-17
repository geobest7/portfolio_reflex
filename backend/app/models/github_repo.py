from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import JSON
from datetime import datetime
from ..database import Base

class GitHubRepo(Base):
    __tablename__ = "github_repos"
    
    id = Column(Integer, primary_key=True, index=True)
    repo_id = Column(Integer, unique=True, index=True)  # GitHub repo ID
    name = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    html_url = Column(String, nullable=False)
    homepage = Column(String, nullable=True)
    language = Column(String, nullable=True)
    stargazers_count = Column(Integer, default=0)
    forks_count = Column(Integer, default=0)
    topics = Column(JSON, nullable=True)  # Array de strings
    created_at = Column(String, nullable=True)
    updated_at = Column(String, nullable=True)
    pushed_at = Column(String, nullable=True)
    
    # Cache metadata
    cached_at = Column(DateTime, default=datetime.utcnow)
    activo = Column(Boolean, default=True)