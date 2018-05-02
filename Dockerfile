FROM maestroserver/maestro-python-gcc
MAINTAINER Felipe Signorini <felipe.signorini@maestroserver.io>

ENV APP_PATH=/opt/application
RUN pip3 install gunicorn

WORKDIR $APP_PATH

COPY ./app $APP_PATH/app
COPY ./instance $APP_PATH/instance
COPY requirements.txt requirements.txt
COPY package.json package.json
COPY run.py $APP_PATH/run.py
COPY gunicorn_config.py /opt/gunicorn_config.py

RUN pip3 install -r requirements.txt

CMD ["/usr/bin/gunicorn", "--config", "/opt/gunicorn_config.py", "run:app"]
