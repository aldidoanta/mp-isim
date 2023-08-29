# Build stage
FROM maven:3.9.3-amazoncorretto-17 AS build
COPY src /home/app/src
COPY pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package

# Package stage
FROM openjdk:17-alpine
COPY --from=build /home/app/target/dummy-0.0.1-SNAPSHOT.jar /usr/local/lib/dummy.jar
EXPOSE 8004
ENTRYPOINT ["java","-jar","/usr/local/lib/dummy.jar"]