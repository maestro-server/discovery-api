FROM maestroserver/maestro-python-gcc

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
RUN addgroup app && adduser -S app

ENV APP_PATH=/opt/application

WORKDIR $APP_PATH

COPY ./app $APP_PATH/app
COPY ./instance $APP_PATH/instance
COPY requirements.txt requirements.txt
COPY package.json package.json
COPY run.py $APP_PATH/run.py
COPY gunicorn_config.py /opt/gunicorn_config.py

RUN pip3 install --upgrade pip gunicorn
RUN pip3 install -r requirements.txt

RUN apk del --no-cache --purge .build-deps \
RUN rm -rf /var/cache/apk/*

ENTRYPOINT ["/sbin/tini","-g","--"]
CMD ["docker-entrypoint.sh"]