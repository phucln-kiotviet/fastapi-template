from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from . import service, schemas
from ..dependency import get_db
from uuid import UUID


router = APIRouter()


@router.get("/", response_model=Page[schemas.Articles], tags=['list articles'])
def get_list_articles(db: Session = Depends(get_db)):
    return paginate(service.get_list_articles(db))


@router.get("/{articles_id}", response_model=schemas.Articles, tags=['CRUD articles'])
def get_articles(articles_id: UUID, db: Session = Depends(get_db)):
    return service.get_articles(db=db, articles_id=articles_id)


# @router.post("/", response_model=schemas.Articles, status_code=status.HTTP_201_CREATED, tags=['CRUD articles'])
@router.post("/", status_code=status.HTTP_201_CREATED, tags=['CRUD articles'])
def create_articles(
    articles: schemas.ArticlesCreate, db: Session = Depends(get_db)
):
    return service.create_articles(db=db, articles=articles)


@router.patch("/{articles_id}", response_model=schemas.ArticlesUpdate, tags=['CRUD articles'])
def update_articles(
    articles_id: UUID,
    update_fields: schemas.ArticlesUpdate,
    db: Session = Depends(get_db)
):
    return service.update_articles(db, articles_id=articles_id, updated_fields=update_fields)


@router.delete("/{articles_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['CRUD articles'])
def delete_articles(articles_id: UUID, db: Session = Depends(get_db)):
    return service.delete_articles(db=db, articles_id=articles_id)
