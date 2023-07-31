FROM python:3.10.6-slim-bullseye

WORKDIR /vocabulary_hub

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /vocabulary_hub:$PYTHONPATH

COPY . /vocabulary_hub/

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["python", "/vocabulary_hub/manage.py", "runserver", "0.0.0.0:8000"]
