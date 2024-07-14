FROM python:3.12-slim-bullseye

RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN pip install --upgrade setuptools

RUN poetry config virtualenvs.create false

WORKDIR /code

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry install --no-dev

COPY ./gunicorn_conf.py .
COPY ./app ./app
COPY ./alembic.ini .
COPY ./main.py .

COPY "./docker_entrypoint.sh" .
RUN chmod +x "./docker_entrypoint.sh"

ENTRYPOINT ["./docker_entrypoint.sh"]
