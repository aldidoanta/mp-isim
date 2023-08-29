# Matcher - Similarity Flooding

A Matcher implementation using [Similarity Flooding](https://doi.org/10.1109/ICDE.2002.994702) algorithm.

The implementation was adapted from [Valentine](https://doi.org/10.1109/ICDE51399.2021.00047), a Python package to perform schema matching using `pandas DataFrame`.

User can perform the schema matching operation via REST web service.

## Running the Web Service
```bash
python manage.py runserver 8003
```

## OpenAPI 3.0 Documentation
- Schema in JSON: http://localhost:8003/docs/schema
- Rendered using Swagger UI: http://localhost:8003/docs

## Technology Stack
1. REST web service: Python + [Django](https://www.djangoproject.com/) + [Django REST framework](https://www.django-rest-framework.org/)
2. OpenAPI 3.0 schema generator: [drf-spectacular](https://github.com/tfranzel/drf-spectacular)
