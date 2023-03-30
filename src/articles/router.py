from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from . import service, schemas
from ..dependency import get_db


router = APIRouter()


@router.get("/")
def get_list_articles(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    return service.get_list_articles(db, skip=skip, limit=limit)


@router.get("/{articles_id}", response_model=schemas.Articles)
def get_articles(articles_id: int, db: Session = Depends(get_db)):
    return service.get_articles(db=db, articles_id=articles_id)


@router.post("/", response_model=schemas.Articles, status_code=status.HTTP_201_CREATED)
def create_articles(
    articles: schemas.Articles, db: Session = Depends(get_db)
):
    return service.create_articles(db=db, articles=articles)


@router.delete("/{articles_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_articles(articles_id: int, db: Session = Depends(get_db)):
    return service.delete_articles(db=db, articles_id=articles_id)


@router.patch("/{articles_id}", response_model=schemas.ArticlesUpdate)
def update_articles(
    articles_id: int,
    update_fields: schemas.ArticlesUpdate,
    db: Session = Depends(get_db)
):
    return service.update_articles(db, articles_id=articles_id, updated_fields=update_fields)
