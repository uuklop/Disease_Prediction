# Disease Prediction (Django + ML)

A small Django web app that demonstrates disease prediction and basic doctor/patient features using a scikit-learn model.

## Quick overview

- Django backend with multiple apps: `accounts`, `chats`, `drug_recommendation`, `main_app`.
- Pretrained ML models are included in the repo (`medical_model.pkl`, `medical_nb.pkl`) and a `trained_model/` directory.
- Screenshots are in `screenshots/` and images are in `pics/` for visual documentation.

## Demo screenshots

![Home](/screenshots/Capture1.PNG)

![Prediction](/screenshots/Capture2.PNG)

![Chat / Consultation](/screenshots/Capture3.PNG)

(If images don't display on GitHub, ensure they are committed in the `screenshots/` folder.)

## What you'll find in this repository

- `manage.py` — Django management script
- `disease_prediction/` — project settings and wsgi
- `accounts/`, `chats/`, `drug_recommendation/`, `main_app/` — Django apps
- `requirements.txt` — pinned Python dependencies
- `medical_model.pkl`, `medical_nb.pkl`, `trained_model/` — ML artifacts
- `db.sqlite3` — example SQLite DB (optional)

## Recommended workflow (local development)

Pick one of the following database options:

Option A — Quick start with SQLite (recommended for testing)

1. Create and activate a virtualenv:

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations and create a superuser:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Start the development server:

```bash
python manage.py runserver
```

Navigate to http://127.0.0.1:8000/ and log in with the superuser.

Option B — Use PostgreSQL (matches original `settings.py`)

Install system deps (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install -y build-essential libpq-dev python3-dev postgresql postgresql-contrib
```

Set the `postgres` user's password and create the database (adjust values as needed):

```bash
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'uenr1206';"
sudo -u postgres psql -c "CREATE DATABASE predico;"
```

Then follow steps to create a venv, install dependencies, run migrations and start the server (same as SQLite steps above).

## Important notes / security

- `disease_prediction/settings.py` currently includes an email password and DEBUG=True. Remove secrets before publishing or move them to environment variables. Example using envvars in a shell or `.env` file (use `python-decouple` or `django-environ` for production).
- Large binary model files (e.g. `medical_model.pkl`) can bloat Git history. Consider using Git LFS or a model hosting service if you want to keep them out of the main repo.

## Git steps to push to GitHub

1. Initialize and commit locally (if not already a git repo):

```bash
git init
git add .
git commit -m "Initial commit - Disease prediction Django app"
```

2. Create a repo on GitHub (via website) and add it as remote (example):

```bash
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

If files like model pickles are large, follow GitHub's guidance for Git LFS:

```bash
git lfs install
git lfs track "*.pkl"
git add .gitattributes
git add <large files>
git commit -m "Add models via LFS"
git push
```

## Troubleshooting

- If `pip install -r requirements.txt` fails on `psycopg2`, install `libpq-dev` and Python dev headers (see PostgreSQL step).
- If static files look incorrect, run `python manage.py collectstatic` (not necessary for dev server with DEBUG=True).

## License

This project includes an existing `LICENSE` file — review it before publishing.

## Contributing

If you want, I can:
- Create a cleaned `settings_example.py` that reads secrets from environment variables.
- Add a short CONTRIBUTING.md with how to run tests and report issues.
- Move heavy model files to Git LFS and add instructions.

---

If you'd like I can now:
- Create/update a `.gitignore` to exclude virtualenvs and sensitive files and commit it.
- Create `settings_example.py` and remove secrets from the committed `settings.py`.
- Initialize git and push to a remote if you provide the remote URL.

Tell me which next step to do.
