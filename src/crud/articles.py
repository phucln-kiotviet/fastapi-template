from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def get_list_articles():
    return [1, 2, 3, 4, 5]
