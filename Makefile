start:
	poetry run gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

install:
	poetry install