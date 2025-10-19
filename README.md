<<<<<<< HEAD
# Disease Prediction (Django + ML)

A small Django web app that demonstrates disease prediction and basic doctor/patient features using a scikit-learn model.

## Quick overview

- Django backend with multiple apps: `accounts`, `chats`, `drug_recommendation`, `main_app`.
- Pretrained ML models are included in the repo (`medical_model.pkl`, `medical_nb.pkl`) and a `trained_model/` directory.
- Screenshots are in `screenshots/` and images are in `pics/` for visual documentation.

## Demo screenshots

### Screenshots

Below are the UI screenshots from the `screenshots/` folder. Click images to view the full-size version on GitHub.

[![Capture1](/screenshots/Capture1.PNG)](/screenshots/Capture1.PNG)
[![Capture2](/screenshots/Capture2.PNG)](/screenshots/Capture2.PNG)
[![Capture3](/screenshots/Capture3.PNG)](/screenshots/Capture3.PNG)
[![Capture4](/screenshots/Capture4.PNG)](/screenshots/Capture4.PNG)
[![Capture5](/screenshots/Capture5.PNG)](/screenshots/Capture5.PNG)

[//]: # (Main README for the Disease Prediction project)

# Disease Prediction (Django + ML)

A Django web application that demonstrates disease prediction and drug recommendation using pretrained scikit-learn models and a small suite of Django apps for doctor/patient workflows.

## Quick overview

- Django backend with multiple apps: `accounts`, `chats`, `drug_recommendation`, `main_app`.
- Pretrained ML artifacts included: `medical_model.pkl`, `medical_nb.pkl` and a `trained_model/` directory.
- UI assets and screenshots live in `templates/`, `pics/`, and `screenshots/`.

## Seminar paper — key points (summary)
The repository contains a companion seminar paper ("Seminar Paper.pdf", author: James Polkuu) that documents the research and experiments behind the models. Vital takeaways below.

- Abstract: The paper evaluates multiple machine learning classifiers (Decision Tree, Logistic Regression, Random Forest, XGBoost, SVM, Naive Bayes) for disease prediction and drug recommendation. Results show these models can deliver high accuracy and useful recommendations when trained on curated medical records.

- Datasets:
	- Disease dataset: each CSV has 133 columns (132 symptom columns + 1 prognosis column). Symptoms map to 42 disease classes.
	- Drug dataset: columns include age, disease, gender, and drug; includes mappings from diseases to prescribed drugs (4955 drug records covering 9 diseases in the dataset used by the authors).

- Methods: The study trains and compares Decision Tree, Logistic Regression, Random Forest, XGBoost, Support Vector Machine, and Naive Bayes classifiers. Models were evaluated with standard classification metrics (accuracy, precision, recall, F1-score).

- Results: Reported experiments indicate high accuracy and strong precision/recall across the tested models, supporting the feasibility of automated disease prediction and drug recommendation from structured symptom records.

- Recommendation & notes: The paper recommends integrating such a system into clinical workflows with care for data privacy, model interpretability, and ethical considerations. Authors advise further work on additional algorithms and deployment safeguards.

## What you'll find in this repository

- `manage.py` — Django management script
# Disease Prediction (Django + ML)

A Django web application that demonstrates disease prediction and drug recommendation using pretrained scikit-learn models and a small suite of Django apps for doctor/patient workflows.

## Quick overview

- Django backend with multiple apps: `accounts`, `chats`, `drug_recommendation`, `main_app`.
- Pretrained ML artifacts included: `medical_model.pkl`, `medical_nb.pkl` and a `trained_model/` directory.
- UI assets and screenshots live in `templates/`, `pics/`, and `screenshots/`.

## Seminar paper — key points (summary)
The repository contains a companion seminar paper ("Seminar Paper.pdf", author: James Polkuu) that documents the research and experiments behind the models. Vital takeaways below.

- Abstract: The paper evaluates multiple machine learning classifiers (Decision Tree, Logistic Regression, Random Forest, XGBoost, SVM, Naive Bayes) for disease prediction and drug recommendation. Results show these models can deliver high accuracy and useful recommendations when trained on curated medical records.

- Datasets:
	- Disease dataset: each CSV has 133 columns (132 symptom columns + 1 prognosis column). Symptoms map to 42 disease classes.
	- Drug dataset: columns include age, disease, gender, and drug; includes mappings from diseases to prescribed drugs (4955 drug records covering 9 diseases in the dataset used by the authors).

- Methods: The study trains and compares Decision Tree, Logistic Regression, Random Forest, XGBoost, Support Vector Machine, and Naive Bayes classifiers. Models were evaluated with standard classification metrics (accuracy, precision, recall, F1-score).

- Results: Reported experiments indicate high accuracy and strong precision/recall across the tested models, supporting the feasibility of automated disease prediction and drug recommendation from structured symptom records.

- Recommendation & notes: The paper recommends integrating such a system into clinical workflows with care for data privacy, model interpretability, and ethical considerations. Authors advise further work on additional algorithms and deployment safeguards.

### Experiment/Dataset
In order to assess the effectiveness of our proposed system, we employed a comprehensive dataset sourced from Kaggle, consisting of curated medical records.

Disease Dataset
The dataset consists of two CSV files: one for training and one for testing the model. Each file contains 133 columns, where 132 columns represent symptoms and the last column represents the prognosis. The symptoms are mapped to 42 diseases.

Drug Dataset
The drugs dataset consists of a single CSV file with 4 columns. Three columns represent age, disease, and gender, while the last column indicates the corresponding drug. A total of 9 diseases are mapped to 4955 drugs in this dataset.

We apply Decision Tree, Logistic Regression, Random Forest, XGBoost, Support Vector Machine, and Naive Bayes algorithms.

### Results
Experimental results demonstrate the effectiveness of the employed machine learning algorithms for disease prediction and drug recommendation. The models achieve high accuracy, precision, recall, and F1-score, indicating their ability to identify diseases accurately.

## What you'll find in this repository

- `manage.py` — Django management script
- `disease_prediction/` — project settings and WSGI
- `accounts/`, `chats/`, `drug_recommendation/`, `main_app/` — Django apps
- `requirements.txt` — pinned Python dependencies
- `medical_model.pkl`, `medical_nb.pkl`, `trained_model/` — ML artifacts
- `db.sqlite3` — example SQLite DB (optional)

## Recommended workflow (local development)

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

Option B — Use PostgreSQL (matches `disease_prediction/settings.py`)

Install system deps (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install -y build-essential libpq-dev python3-dev postgresql postgresql-contrib
```

Create DB / user or update `DATABASES` in settings to match your environment.

## Important notes / security

- `disease_prediction/settings.py` currently contains hard-coded secrets (SECRET_KEY, email credentials, and a DB password) and `DEBUG = True`. Move secrets to environment variables before publishing or deploying.
- Large model files (`*.pkl`) can bloat the repo. Consider Git LFS or external model storage for production.

## Git / publishing notes

- If you add large binaries, use Git LFS:

```bash
git lfs install
git lfs track "*.pkl"
git add .gitattributes
git add <large files>
git commit -m "Add models via LFS"
git push
```

## Troubleshooting

- If `pip install -r requirements.txt` fails on `psycopg2`, install `libpq-dev` and Python headers (see PostgreSQL step).
- If static files look incorrect, run `python manage.py collectstatic` (not necessary for dev server when `DEBUG=True`).

## License

See `LICENSE` in the repository.

## Contributing ideas

- Create a `settings_example.py` or refactor settings to use environment variables.
- Add a small test that loads the pickled models and runs a smoke prediction to validate compatibility with pinned `scikit-learn`.
- Add `.gitignore` entries for virtualenvs, IDE files, and large artifacts.

---

_Seminar paper author: James Polkuu (file: `Seminar Paper.pdf`)._
