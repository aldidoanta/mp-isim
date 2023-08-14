# Matcher - Dummy

A Dummy Matcher that returns a static response.

User can perform the schema matching operation via the REST web service.

## Running the Web Service
```bash
./mvnw clean spring-boot:run
```

## OpenAPI 3.0 Documentation
- Schema in JSON: http://localhost:8080/docs/schema
- Rendered using Swagger UI: http://localhost:8080/docs

## Technology Stack
1. REST web service: Java + [Spring Boot](https://spring.io/projects/spring-boot)
2. OpenAPI 3.0 schema generator: [springdoc-openapi](https://springdoc.org/)
