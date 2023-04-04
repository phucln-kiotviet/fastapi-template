import os
import json
from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from uuid import UUID
from ..producer import channel
from dotenv import load_dotenv


load_dotenv()
ANSIBLE_QUEUE = os.getenv('ANSIBLE_QUEUE')


def get_articles(db: Session, articles_id: UUID):
    db_articles = db.query(models.Articles).filter(
        models.Articles.id == articles_id,
        models.Articles.deleted == None
    ).first()
    if not db_articles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No articles with id:  {}".format(articles_id))
    return db_articles


def get_list_articles(db: Session):
    return db.query(models.Articles).filter(models.Articles.deleted == None).all()


def create_articles(db: Session, articles: schemas.ArticlesCreate):
    # db_articles = models.Articles(**articles.dict())
    # db.add(db_articles)
    # db.commit()
    # db.refresh(db_articles)
    # return db_articles
    channel.basic_publish(exchange='', routing_key=ANSIBLE_QUEUE,
                          body=json.dumps({"name": "ansible executor"}))
    return "Ok"


def update_articles(db: Session, articles_id: UUID, updated_fields: schemas.ArticlesUpdate):
    articles_query = db.query(models.Articles).filter(
        models.Articles.id == articles_id,
        models.Articles.deleted == None
    )
    db_articles = articles_query.first()

    if not db_articles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No articles with id:  {}".format(articles_id))
    update_data = updated_fields.dict(exclude_unset=True)
    articles_query.filter(models.Articles.id == articles_id).update(
        update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_articles)
    return db_articles


def delete_articles(db: Session, articles_id: UUID):
    articles_query = db.query(models.Articles).filter(
        models.Articles.id == articles_id,
        models.Articles.deleted == None)
    articles = articles_query.first()

    if not articles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No articles with id:  {}".format(articles_id))
    articles_query.update({"deleted": datetime.now()},
                          synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
