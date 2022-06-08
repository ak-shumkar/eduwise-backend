compose dev:
	docker-compose up -d
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
