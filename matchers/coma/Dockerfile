# FROM python:3.10.6-slim-bullseye

# # Install Java to run COMA's jar
# RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2
# # RUN rmdir /etc/ssl/certs/java
# # RUN mkdir /etc/ssl/certs/java

# RUN apt update
# RUN apt install --only-upgrade ca-certificates ca-certificates-java 
# RUN apt install -y --no-install-recommends \
#         openjdk-17-jre-headless
# # Prints installed java version, just for checking
# RUN java --version


# WORKDIR /coma

# ENV PYTHONUNBUFFERED 1
# ENV PYTHONPATH /coma:$PYTHONPATH

# COPY . /coma/

# EXPOSE 8000

# RUN pip install -r requirements.txt

# CMD ["python", "/coma/manage.py", "runserver", "0.0.0.0:8000"]

FROM openjdk:17-alpine

# # Install Java
# RUN apk update \
# && apk upgrade \
# && apk add --no-cache bash \
# && apk add --no-cache --virtual=build-dependencies unzip \
# && apk add --no-cache curl \
# && apk add --no-cache openjdk17-jre-headless

# Install Python
RUN apk add --no-cache python3 \
&& python3 -m ensurepip \
&& pip3 install --upgrade pip setuptools \
&& rm -r /usr/lib/python*/ensurepip && \
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache

# Install Python dependencies and run the app
WORKDIR /coma

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /coma:$PYTHONPATH

COPY . /coma/

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["python", "/coma/manage.py", "runserver", "0.0.0.0:8000"]
