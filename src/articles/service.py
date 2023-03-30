from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi import HTTPException
from . import models, schemas


def get_articles(db: Session, articles_id: int):
    return db.query(models.Articles).get(articles_id)


def get_list_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Articles).offset(skip).limit(limit).all()


def create_articles(db: Session, articles: schemas.Articles):
    db_articles = models.Articles(**articles.dict())
    db.add(db_articles)
    db.commit()
    db.refresh(db_articles)
    return db_articles


def update_articles(db: Session, articles_id: int, updated_fields: schemas.ArticlesUpdate):
    db.execute(
        update(models.Articles)
        .where(models.Articles.id == articles_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields


def delete_articles(db: Session, articles: schemas.Articles):
    db.delete(articles)
    db.commit()
    return "deleted"
