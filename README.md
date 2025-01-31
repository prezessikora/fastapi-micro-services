Mono-repo with micro-services based on FastAPI.

The services are dockerized and the whole setup with RabbitMQ and MongoDB are brought up with docker-compose.

This ia a playground to discover seams and find service boundaries.

Separate stage splits this mono-repo into separate repositories.

# With each dependencies change

pip freeze > requirements.txt

# Docker

docker build -t myimage .

docker run -d --name mycontainer -p 80:80 myimage

# Pytest

Remember to:
PYTHONPATH=.
export PYTHONPATH
