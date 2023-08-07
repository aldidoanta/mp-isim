FROM openjdk:17-alpine

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
