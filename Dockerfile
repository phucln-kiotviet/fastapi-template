FROM python:3.10-slim

WORKDIR /usr/src/app

# set environment variables => check y nghia :d
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .


# CMD ["alembic upgrade head;uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]