# chemlab

Repo for [https://lab.sin.org.pl/](https://lab.sin.org.pl/)

## stack

* Python 3.5
* Django 1.11
* Bootstrap 4

## Installation

1. Create [virtual environment](https://realpython.com/blog/python/python-virtual-environments-a-primer/) and enter it.
2. Install dependencies:
        $ pip install -r requirements.txt

3. Copy `env.example` file as `.env`:
```
$ cp chemlab/_core/env.example chemlab/_core/.env
```

    and fill it with desired settings (`DJANGO_SECRET_KEY` for sure). We are using [django-environ](https://github.com/joke2k/django-environ) to keep our settings nice and tidy.
4. Migrate the database:
        $ python manage.py migrate
5. Download drugs data:
        $ python manage.py get_drugs

6. Run the development server:
        $ python manage.py runserver

## Contributing

Fork this repository and submit your PRs to `master` branch.

If something's wrong - open an issue.
