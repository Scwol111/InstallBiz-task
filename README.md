# InstallBiz-task
Task for InstallBiz company.

Task: create auth service with FastApi

## Setup
- ### Docker setup
    - Run `docker-compose up -d` to creating docker contaiers with project
        - Will be created three contaners:
            - __postgres__ - db container
            - __migrator__ - container to apply new migrations to db
            - __api_service__ - main container with fastapi service
    - You can access to project's api swagger on http://localhost:8000/docs

- ### local setup
    - install poetry with `pip install poetry`
    - install requrements with `poetry install`
    - customize __*.env*__ file with your data
    - run `fastapi dev main.py` to development mode
    - or run `uvicorn main:app` to run in production mode

## Project explanation
This is simple auth service that can be easily self extended or integrated to any fastapi projects

- ### Work with project

    After run service you have access to two auth and two test methods:

    - `/auth/register` - will create new user in database. Login must be uniquie in table. Password should be more or equal than 20 symbols
    - `/auth/login` - auth with same login-password from `/auth/register` and you will have jwt token for next connections
    - `/test/say_hello` - simple test method. Just return `Hello world` string without anything
    - `/test/say_hello_auth` - another simple test method. Return same as `/test/say_hello`, but you must be authenticated with Bearer token from `/auth/login`

- ### Project folders
    - __*alembic*__ - contain models migrations for database
    - __*api*__ - main api folders. Contains all api controllers
        - __*api_utils*__ - contain simple methods library, but with some project imports
        - __*schemas*__ - contain Pydantic shemas of project
    - __*database*__ - contains classes and methods to work with database
    - __*models*__ - contains sqlalchemy orm models
    - __*utils*__ - contains simple methods library. You can easily use this without any another project importa
