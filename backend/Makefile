build:
	docker-compose build

up: run

run: build
	echo Starting local development dependencies
	docker-compose up -d
	docker-compose logs -f

down: stop

stop:
	docker-compose down

logs:
	docker-compose logs -f

clean-venv:
	rm -r .venv
	make venv

venv:
	poetry config virtualenvs.in-project true && \
	poetry config virtualenvs.path "./.venv" && \
	poetry env use 3.9 && \
	poetry update || \
	poetry install

format:
	poetry run black .

test:
	poetry run pytest .

makemigrations:
	docker-compose run web alembic revision --autogenerate

migrate:
	docker-compose run web alembic upgrade head