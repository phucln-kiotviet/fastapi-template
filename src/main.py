import uvicorn
from fastapi import FastAPI
from .articles import router as articles


app = FastAPI()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/health")
def health_check():
    return {"message": "ok"}


# this imports the route in other service
app.include_router(articles.router, prefix="/articles")
