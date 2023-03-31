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


## Database

- Create postgres container:

```
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:15-alpine
```

- Create database in postgres:

```
create database articles;
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

- Generate script to create table `Articles` by alembic command:

```
alembic revision --autogenerate -m "Adding Articles Table"
```
- Create table with command: 

```
alembic upgrade head
```


## Run service
- Use script:

```
bash run.sh
```

- Or you can use IDE: vscode (F5).

- Access localhost: `http://127.0.0.1:8000/docs` to check api documents.