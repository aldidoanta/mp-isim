FROM python:3.10.12-slim-bullseye

WORKDIR /similarity_flooding

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /similarity_flooding:$PYTHONPATH

COPY . /similarity_flooding/

EXPOSE 8003

RUN pip install -r requirements.txt

CMD ["python", "/similarity_flooding/manage.py", "runserver", "0.0.0.0:8003"]
