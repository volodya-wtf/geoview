#!/usr/bin/make

include .env

SHELL = /bin/sh
CURRENT_UID := $(shell id -u):$(shell id -g)

export CURRENT_UID

BACKEND_CONTAINER = oort_backend


export BACKEND_CONTAINER

up:
	docker-compose up -d --force-recreate --build --remove-orphans 
down:
	docker-compose down
sh:
	docker exec -it /$(BACKEND_CONTAINER) /bin/sh
migrations:
	docker exec -it /$(BACKEND_CONTAINER) python3 manage.py makemigrations
su:
	docker exec -it /$(BACKEND_CONTAINER) python3 manage.py createsuperuser
logsb:
	docker logs /$(BACKEND_CONTAINER) -f
logs:
	docker-compose logs -f
volumes:
	docker volume create oort_db_data
clear:
	make down
	docker volume rm oort_db_data
