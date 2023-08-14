# Matcher - COMA

A Matcher using [COMA 3.0 from the University of Leipzig](https://dbs.uni-leipzig.de/Research/coma.html).

The implementation was adapted from [Valentine](https://doi.org/10.1109/ICDE51399.2021.00047), a Python package to perform schema matching using pandas DataFrame.

User can perform the schema matching operation via the REST web service.

## Running the Web Service
```bash
python manage.py runserver 8001
```

## OpenAPI 3.0 Documentation
- Schema in JSON: http://localhost:8001/docs/schema
- Rendered using Swagger UI: http://localhost:8001/docs

## Technology Stack
1. REST web service: Python + [Django](https://www.djangoproject.com/) + [Django REST framework](https://www.django-rest-framework.org/)
2. OpenAPI 3.0 schema generator: [drf-spectacular](https://github.com/tfranzel/drf-spectacular)
