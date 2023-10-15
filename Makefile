MANAGE := poetry run python3 manage.py
PORT := 8000

dev:
	poetry run python3 manage.py runserver 0.0.0.0:8000

start:
	gunicorn tenis_tasks.wsgi --bind 0.0.0.0:$(PORT)

install:
	@poetry install
	apt-get install ffmpeg libavcodec-extra

lint:
	@poetry run flake8 tenis_tasks

.PHONY: start install lint dev