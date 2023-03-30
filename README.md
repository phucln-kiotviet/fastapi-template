# FastAPI template

- Should use python3.10 to get best syntax

## Virtual Env



- Create `venv`:
```
python3 -m venv venv
```

- Add new package:

```
pip3 install <packagename>
```

- Install packages:

```
pip3 install -r requirements.txt
```


## Debugging

- Create postgres container:

```
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:15-alpine
```

## Alembic

- If we have multiple models we can config `target_metadata` in `/migrations/env.py` like this:

```
target_metadata = [articles_models.Base.metadata, categories_models.Base.metadata]
```



- Create migrations folder with `alembic` command:

```
alembic init migrations
```


- Create database in postgres:

```
create database articles;
```


- Generate script to create table `Articles` by alembic command:

```
alembic revision --autogenerate -m "Adding Articles Table"
```
- Create table with command: 

```
alembic upgrade head
```