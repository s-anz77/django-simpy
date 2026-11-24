# Simpy Community Platform

A Django community website for publishing and browsing articles, managing user profiles, and contacting the site through a message form.

**Live demo:** [simpy.up.railway.app](https://simpy.up.railway.app/)

## Features

- Browse the latest articles and view articles by author.
- Register, sign in, update a profile, and reset a password.
- Create articles and edit or delete your own articles.
- Upload a profile image; images are resized to fit within 256 × 256 pixels.
- Send a message through the contact form.
- Browse paginated article lists.

## Tech stack

- Python 3.15
- Django 6.1
- SQLite
- Pillow for profile image handling
- WhiteNoise and Gunicorn for deployment

## Prerequisites

- Python 3.15
- pip

## Local setup

From the repository root, create and activate a virtual environment, then install the pinned dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies and initialize the database:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>.

## Configuration

The project uses SQLite (`db.sqlite3`) as its database.

The following environment variables are used to configure Django:

| Variable | Description | Default |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django secret key | Required |
| `DJANGO_DEBUG` | Enables or disables debug mode | `false` |

The application requires `DJANGO_SECRET_KEY` to be set in the environment. If it is missing, Django raises a configuration error.

For Railway deployment, configure these variables in the service's **Variables** settings. Never commit secret values to the repository.

Uploaded profile images are stored in the `media/` directory during local development.

## Project structure

- `firstdjangoproject/` — Django project settings, URL configuration, and WSGI/ASGI entry points.
- `blog/` — article and contact-message models, views, forms, and templates.
- `users/` — registration, authentication, and user profile functionality.
- `static/` — CSS, JavaScript, icons, and images.
- `manage.py` — Django management commands.

