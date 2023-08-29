FROM python:3.10.12-slim-bullseye

WORKDIR /cupid

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /cupid:$PYTHONPATH

COPY . /cupid/

EXPOSE 8002

RUN pip install -r requirements.txt

CMD ["python", "/cupid/manage.py", "runserver", "0.0.0.0:8002"]
