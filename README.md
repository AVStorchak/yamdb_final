# API-Yamdb

API service for the Yamdb website, which is intended for publishing reviews about different artworks.

[![Actions Status](https://github.com/AVStorchak/yamdb_final/workflows/Yamdb%20workflow/badge.svg)]

## Getting Started

1. Copy the repository

### Prerequisites

Nothing, as the project uses the Docker system.

### Installing

1. Open the terminal and run "docker-compose up" from the project directory

2. Open another terminal, run "docker-compose exec web /bin/bash" and then run "python manage.py migrate" to establish the DB. 

3. In order to create the superuser, open another terminal and run "docker-compose exec web /bin/bash" (skip if such a terminal already is opened), then run "python manage.py createsuperuser" and follow the instructions. The administrator page is accessible at http://127.0.0.1:8000/admin/.

4. In order to fill out the database with initial data, open another terminal and run "docker-compose exec web /bin/bash" (skip if such a terminal already is opened), then run python manage.py loaddata fixtures.json

## Running the tests

None

### Break down into end to end tests

None

### And coding style tests

None

## Deployment

None

## Built With

Django, Postgresql, Docker

## Contributing

None

## Versioning

None

## Authors

* **Andrei Storchak** - *Initial work* - [AVStorchak](https://github.com/AVStorchak/)

## License

None

## Acknowledgments

* Yandex.Praktikum
