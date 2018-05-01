FROM python:alpine3.6
MAINTAINER Felipe Signorini <felipe.signorini@maestroserver.io>

RUN apk add --no-cache --virtual build-base && \
    apk add --no-cache linux-headers

ENV APP_PATH=/opt/application
RUN pip3 install --upgrade pip gunicorn

WORKDIR $APP_PATH

COPY ./app $APP_PATH/app
COPY ./instance $APP_PATH/instance
COPY requirements.txt requirements.txt
COPY package.json package.json
COPY run.py $APP_PATH/run.py
COPY gunicorn_config.py /opt/gunicorn_config.py

RUN pip3 install -r requirements.txt
RUN apk del build-base

CMD ["/usr/bin/gunicorn", "--config", "/opt/gunicorn_config.py", "--user", "maestro", "run:app"]
