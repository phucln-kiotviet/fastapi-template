from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status, Response
from . import models, schemas


def get_articles(db: Session, articles_id: int):
    return db.query(models.Articles).get(articles_id)


def get_list_articles(db: Session):
    return db.query(models.Articles).filter(models.Articles.deleted == None).all()


def create_articles(db: Session, articles: schemas.Articles):
    db_articles = models.Articles(**articles.dict())
    db.add(db_articles)
    db.commit()
    db.refresh(db_articles)
    return db_articles


def update_articles(db: Session, articles_id: int, updated_fields: schemas.ArticlesUpdate):
    articles_query = db.query(models.Articles).filter(
        models.Articles.id == articles_id)
    db_articles = articles_query.first()

    if not db_articles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No articles with {articles_id}")
    update_data = updated_fields.dict(exclude_unset=True)
    articles_query.filter(models.Articles.id == articles_id).update(
        update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_articles)
    return db_articles


def delete_articles(db: Session, articles_id: int):
    articles_query = db.query(models.Articles).filter(
        models.Articles.id == articles_id)
    articles = articles_query.first()

    if not articles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No articles with {articles_id}")
    articles_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
