FROM python:3.10-buster

RUN pip install pipenv

COPY ./docker-entrypoint.sh /opt/app/
COPY ./src /opt/app/
COPY log_config.json /opt/app/
COPY Pipfile /opt/app/
COPY Pipfile.lock /opt/app/
COPY .flake8 /opt/app/
COPY mypy.ini /opt/app/
COPY pylama.ini /opt/app/

WORKDIR /opt/app/
ENV PYTHONUNBUFFERED=1

RUN pipenv install --deploy

ENTRYPOINT ["/opt/app/docker-entrypoint.sh" ]
CMD ["pipenv", "run", "uvicorn", "main:app", "--lifespan", "on", "--host", "0.0.0.0", "--log-config", "log_config.json"]
