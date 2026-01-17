from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import httpx
from datetime import datetime, timedelta
from ..database import get_db
from ..models.github_repo import GitHubRepo
from ..schemas.github_repo import GitHubRepoResponse
from ..config import settings

router = APIRouter()

CACHE_TTL_HOURS = 6  # Cache válido por 6 horas


@router.get("/repos", response_model=List[GitHubRepoResponse])
async def get_github_repos(
    force_refresh: bool = False,
    db: Session = Depends(get_db)
):
    """
    Obtener repositorios de GitHub del usuario configurado.
    
    - **force_refresh**: Si es True, ignora el cache y obtiene datos frescos de GitHub
    - Cache TTL: 6 horas
    """
    
    # Verificar cache si no se fuerza refresh
    if not force_refresh:
        cached_repos = db.query(GitHubRepo).filter(
            GitHubRepo.activo == True
        ).all()
        
        if cached_repos:
            # Verificar si el cache es válido (menos de 6 horas)
            oldest_cache = min(repo.cached_at for repo in cached_repos)
            cache_age = datetime.utcnow() - oldest_cache
            
            if cache_age < timedelta(hours=CACHE_TTL_HOURS):
                return cached_repos
    
    # Fetch desde GitHub API
    try:
        headers = {}
        if settings.github_token:
            headers["Authorization"] = f"token {settings.github_token}"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.github.com/users/{settings.github_username}/repos",
                headers=headers,
                params={
                    "sort": "updated",
                    "per_page": 100,
                    "type": "owner"
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Error al obtener repos de GitHub: {response.text}"
                )
            
            repos_data = response.json()
    
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error de conexión con GitHub API: {str(e)}"
        )
    
    # Limpiar cache anterior
    db.query(GitHubRepo).delete()
    db.commit()
    
    # Guardar nuevos repos en cache
    new_repos = []
    for repo_data in repos_data:
        repo = GitHubRepo(
            repo_id=repo_data["id"],
            name=repo_data["name"],
            full_name=repo_data["full_name"],
            description=repo_data.get("description"),
            html_url=repo_data["html_url"],
            homepage=repo_data.get("homepage"),
            language=repo_data.get("language"),
            stargazers_count=repo_data.get("stargazers_count", 0),
            forks_count=repo_data.get("forks_count", 0),
            topics=repo_data.get("topics", []),
            created_at=repo_data.get("created_at"),
            updated_at=repo_data.get("updated_at"),
            pushed_at=repo_data.get("pushed_at"),
            cached_at=datetime.utcnow(),
            activo=True
        )
        db.add(repo)
        new_repos.append(repo)
    
    db.commit()
    
    # Refrescar para obtener IDs generados
    for repo in new_repos:
        db.refresh(repo)
    
    return new_repos


@router.delete("/cache")
def clear_cache(db: Session = Depends(get_db)):
    """Limpiar cache de repositorios de GitHub"""
    deleted = db.query(GitHubRepo).delete()
    db.commit()
    return {"message": f"Cache limpiado. {deleted} repositorios eliminados."}