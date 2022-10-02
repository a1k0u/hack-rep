# hack-rep

download docker

clone repo

download conda


docker container postgresql
```shell
docker run 
  --name hack_postgres 
  -e POSTGRES_PASSWORD=1 
  -d 
  -p 5432:5432
   postgres:alpine
```

```shell
docker exec -it hack_postgres /bin/bash
```

```shell
create database hack;
CREATE USER hack_app WITH PASSWORD '1';
GRANT ALL PRIVILEGES ON DATABASE hack TO hack_app;

\c hack;

psql -h localhost -p 5432 postgres
```

```shell
python3 -m app.db.models
```



## Packages installation
- Create and activate *conda* virtual environment for development:

```shell
conda create -n venv python=3.10
conda activate venv
```

- Install dependencies with Poetry:

```shell
poetry install
```
## Start project
- Run uvicorn with instance of app:

```shell
uvicorn app.main:app --reload
```