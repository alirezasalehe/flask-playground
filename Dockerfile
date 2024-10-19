FROM python:3.9.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src
COPY docker-entrypoint.sh .
WORKDIR src

ARG FLASK_APP
ARG FLASK_ENV
ARG FLASK_DEBUG
ARG FLASK_PORT

RUN chmod +x ../docker-entrypoint.sh
CMD ["../docker-entrypoint.sh"]
