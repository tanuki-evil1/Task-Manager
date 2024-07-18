start:
	poetry run gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

install:
	poetry install

build:
	./build.sh

make-msg:
	poetry run python manage.py makemessages -l en

locale:
	poetry run python manage.py compilemessages --ignore=.venv

shell:
	poetry run python manage.py shell_plus --print-sql
