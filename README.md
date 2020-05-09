[![Codacy Badge](https://api.codacy.com/project/badge/Grade/105fc88179e640d3b7433d24dec6d644)](https://www.codacy.com/app/maestro/discovery-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=maestro-server/discovery-api&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/maestro-server/discovery-api.svg?branch=master)](https://travis-ci.org/maestro-server/discovery-api) 
[![Maintainability](https://api.codeclimate.com/v1/badges/082edc45c4509b79f751/maintainability)](https://codeclimate.com/github/maestro-server/discovery-api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/082edc45c4509b79f751/test_coverage)](https://codeclimate.com/github/maestro-server/discovery-api/test_coverage)
[![Coverage Status](https://coveralls.io/repos/github/maestro-server/discovery-api/badge.svg?branch=master)](https://coveralls.io/github/maestro-server/discovery-api?branch=master)

# Maestro Server #

Maestro Server is an open source software platform for management and discovery servers, apps and system for Hybrid IT. Can manage small and large environments, be able to visualize the latest multi-cloud environment state.

### Demo ###
To test out the demo, [Demo Online](http://demo.maestroserver.io "Demo Online")

## Documentation ##
* [UserGuide](http://docs.maestroserver.io/en/latest/userguide/cloud_inventory/inventory.html "User Guide")
* [API Contract](https://maestro-server.github.io/discovery-api/ "API Contract")

# Maestro Server - Discovery API #

Discovery App is a crawler accountable to connect to cloud providers.

* To manager and authenticate on each cloud provider
* Translate cloud data to maestro data.

![arch](http://docs.maestroserver.io/en/latest/_images/discovery.png)

**Core API:**

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

## Connect to: ##
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
    - "MAESTRO_DATA_URI=http://data:5010"

discovery-celery:
    image: maestroserver/discovery-maestro-celery
    environment:
    - "CELERY_BROKER_URL=amqp://rabbitmq:5672"
    - "MAESTRO_DATA_URI=http://data:5010"
    - "MAESTRO_AUDIT_URI=http://audit:10900"
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

| Env Variables                | Example                  | Description                                |
|------------------------------|--------------------------|--------------------------------------------|
| MAESTRO_DATA_URI             | http://localhost:5005    | Data App - API URL                         |
| MAESTRO_AUDIT_URI            | http://localhost:10900   | Audit App - API URL                        |
| MAESTRO_WEBSOCKET_URI        | http://localhost:8000    | Webosocket App - API URL                   |
|                              |                          |                                            |
| FLASK_ENV                    | development|production   |                                            | 
| MAESTRO_GWORKERS             | 2                        | Gunicorn multi process                     |
| MAESTRO_TRANSLATE_QTD        | 200                      | Prefetch used in translate worker          |
| MAESTRO_COUNTDOWN_LAST       | 10                       | Time in seconds to run the last task       |
| MAESTRO_COUNTDOWN_WS         | 2                        | Delayed time to run ws notification        |
|                              |                          |                                            |
| MAESTRO_SECRETJWT            | XXXX                     | Secret key - JWT for connections           |
| MAESTRO_WEBSOCKET_SECRET     | XXXX                     | Secret Key - JWT Websocket connections     |
| MAESTRO_SECRETJWT_PRIVATE    | XXX                      | Secret Key - JWT private connections       |
| MAESTRO_NOAUTH               | XXX                      | Secret Pass to validate private connections|
|                              |                          |                                            |
| CELERY_BROKER_URL            | XXXX                     | Rabbitmq URL                               |
| CELERYD_TASK_TIME_LIMIT      | 500                      | Timeout - worker                           |

### Contribute ###

Are you interested in developing Maestro Server, creating new features or extending them?

We created a set of documentation, explaining how to set up your development environment, coding styles, standards, learn about the architecture and more. Welcome to the team and contribute with us.

[See our developer guide](http://docs.maestroserver.io/en/latest/contrib.html)

### Contact ###

We may be able to resolve support queries via email. [Please send me a message here](https://maestroserver.typeform.com/to/vf6sGR)

### Donate ###

I have made Maestro Server with my heart, think to solve a real operation IT problem. Its not easy, take time and resources.

The donation will be user to:

- Create new features, implement new providers.
- Maintenance libs, securities flaws, and technical points.

<a href="https://www.buymeacoffee.com/9lVypB7WQ" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

### Sponsor ###

[<img src="docs/_imgs/jetbrains.png" width="100">](https://www.jetbrains.com/?from=maestroserver) 