FROM bitnami/python:3.10-prod-debian-10

RUN apt-get update && apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

ARG UID
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN install_packages build-essential libpq-dev
# Install uWSGI separately before copying requirements.txt
RUN pip install --no-cache-dir uwsgi

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/bash -u "1000" appuser && chown -R appuser /app

RUN chown -R appuser /app
RUN chmod -R ugo+w /app
USER appuser


COPY entrypoint.sh .
COPY server.yaml .
COPY manage.py .
CMD [ "./entrypoint.sh" ]
