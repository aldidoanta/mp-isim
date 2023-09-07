# Matcher - Dummy

A Dummy Matcher that returns an empty array as static response.

User can perform the schema matching operation via the REST web service.

## Installation
### Requirements/Preparations
1. Java 17
2. Docker Engine (optional, for installation with Docker)
3. Make sure the current directory (relative to project root `mp-isim`) is at `/matchers/dummy`.

### Installation without using Docker
```bash
./mvnw clean spring-boot:run
```

### Installation using Docker
1. Download the latest image from Docker Hub.
```bash
docker pull aldidoanta/matcher-dummy:latest
```
2. It is recommended to run the Docker container together with the other containers using [`docker compose.yml`](../../docker-compose.yml). However, it is possible to run an individual Matcher using `docker run`.
```bash
docker run -p 8004:8004 aldidoanta/matcher-dummy
```

## OpenAPI 3.0 Documentation
- Schema in JSON: http://localhost:8004/docs/schema
- Rendered using Swagger UI: http://localhost:8004/docs

## Technology Stack
1. REST web service: Java + [Spring Boot](https://spring.io/projects/spring-boot)
2. OpenAPI 3.0 schema generator: [springdoc-openapi](https://springdoc.org/)
