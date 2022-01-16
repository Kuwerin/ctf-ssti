# For local running
run:
	python -u -m src
# For run via Docker
docker-run:
	docker-compose -p ctf-ssti up --build
