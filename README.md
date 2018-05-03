[![Codacy Badge](https://api.codacy.com/project/badge/Grade/105fc88179e640d3b7433d24dec6d644)](https://www.codacy.com/app/maestro/discovery-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=maestro-server/discovery-api&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/maestro-server/discovery-api.svg?branch=master)](https://travis-ci.org/maestro-server/discovery-api) 
[![Maintainability](https://api.codeclimate.com/v1/badges/082edc45c4509b79f751/maintainability)](https://codeclimate.com/github/maestro-server/discovery-api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/082edc45c4509b79f751/test_coverage)](https://codeclimate.com/github/maestro-server/discovery-api/test_coverage)

# Maestro Server #

Maestro Server is an open source software platform for management and discovery servers, apps and system for Hybrid IT. Can manage small and large environments, be able to visualize the latest multi-cloud environment state.

### Demo ###
To test out the demo, [Demo Online](http://demo.maestroserver.io "Demo Online")

## Documentation ##
* [UserGuide](http://docs.maestroserver.io/en/latest/userguide/cloud_inventory/inventory.html "User Guide")
* [API Contract](https://maestro-server.github.io/discovery-api/ "API Contract")

# Maestro Server - Discovery API #

Discovery App service to connect and crawler provider

- Encharge to manager and authenticate in each provider
- Crawler the data and record into db
- Consume batch insert data

**Core API, organized by modules:**

* API Rest
* Worker - Scan
* Worker - Translate
* Worker - Insert
* Worker - Notification

## TechStack ##
* Python <3.4
* Flask
* Celery
* RabbitMq

## Service relations ##
* Maestro Data

## Setup #

#### Installation by docker ####

```bash
    version: '2'

    services:
    discovery:
        image: maestroserver/discovery-maestro
        ports:
        - "5000:5000"
        environment:
        - "CELERY_BROKER_URL=amqp://rabbitmq:5672"
        - "MAESTRO_DATA_URI=http://data:5000"

    discovery-celery:
        image: maestroserver/discovery-maestro-celery
        environment:
        - "CELERY_BROKER_URL=amqp://rabbitmq:5672"
        - "MAESTRO_DATA_URI=http://data:5000"
```

#### Dev Env ####
```bash
cd devtools/

docker-compose up -d
```

Configure rabbitmq service in .env file

```bash
CELERY_BROKER_URL="amqp://localhost:5672"
CELERYD_TASK_TIME_LIMIT=30
```

Install pip dependences
```bash
pip install -r requeriments.txt
```

Run server
```bash
python -m flask run.py

or

FLASK_APP=run.py FLASK_DEBUG=1 flask run

or 

npm run server
```

Run workers
```bash
celery -A app.celery worker -E -Q discovery --hostname=discovery@%h --loglevel=info

    or 

    npm run celery
```

Run all tests 
```bash
python -m unittest discover
```

Create doc
```bash
npm install
apidoc -i app/controller/ -o docs/
```

### Env variables ###

| Env Variables                | Example                  | Description                        |
|------------------------------|--------------------------|------------------------------------|
| MAESTRO_DATA_URI             | http://localhost:5005    | Data Layer API URL                 |
| NODE_ENV                     | development|production   |                                    | 
| MAESTRO_GWORKERS             | 2 |  DB string connection| Gunicorn multi process             |
| MAESTRO_SECRETJWT            | XXXX                     | Secret key - JWT                   |
| CELERY_BROKER_URL            | XXXX                     | Rabiitmq URL                       |
| MAESTRO_TRANSLATE_QTD        | 200                      | Prefetch used in translate worker  |
| CELERYD_TASK_TIME_LIMIT      | 500                      | Timeout - worker                   |

### Contribute ###

Are you interested in developing Maestro Server, creating new features or extending them?

We created a set of documentation, explaining how to set up your development environment, coding styles, standards, learn about the architecture and more. Welcome to the team and contribute with us.

[See our developer guide](http://docs.maestroserver.io/en/latest/contrib.html)