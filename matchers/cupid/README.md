# Matcher - Cupid

A Matcher implementation using [Cupid](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.79.4079&rep=rep1&type=pdf).

The implementation was adapted from [Valentine](https://doi.org/10.1109/ICDE51399.2021.00047), a Python package to perform schema matching using [`pandas DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).

User can perform the schema matching operation via the REST web service.

## Installation
### Requirements/Preparations
1. Python 3
2. Docker Engine (optional, for installation with Docker)
3. Make sure the current directory (relative to project root `mp-isim`) is at `/matchers/cupid`.
4. Create an environment variable file called `.env` using a template from [`.env.template`](.env.template).

### Installation without using Docker
1. Create and activate the virtual environment.
```bash
python3 -m venv env
source env/bin/activate
```

2. Install app dependencies.
```bash
pip install -r requirements.txt
```

3. Run the Django server.
```bash
python3 manage.py runserver 8002
```

4. To stop and deactivate the virtual environment, <kbd>CTRL</kbd>+<kbd>C</kbd> then:
```bash
deactivate
```

### Installation using Docker
1. Download the latest image from Docker Hub.
```bash
docker pull aldidoanta/matcher-cupid:latest
```
2. It is recommended to run the Docker container together with the other containers using [`docker compose.yml`](../../docker-compose.yml). However, it is possible to run an individual Matcher using `docker run`.
```bash
docker run --env-file .env -p 8002:8002 aldidoanta/matcher-cupid
```

## OpenAPI 3.0 Documentation
- Rendered using Swagger UI: http://localhost:8002/docs

## Technology Stack
1. REST web service: Python + [Django](https://www.djangoproject.com/) + [Django REST framework](https://www.django-rest-framework.org/)
2. OpenAPI 3.0 schema generator: [drf-spectacular](https://github.com/tfranzel/drf-spectacular)
