start:
	poetry run gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

install:
	poetry install

build:
	./build.sh

make-msg:
	poetry run python manage.py makemessages -l ru

locale:
	poetry run python manage.py compilemessages --ignore=.venv

shell:
	poetry run python manage.py shell_plus --print-sql

make-mig:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py