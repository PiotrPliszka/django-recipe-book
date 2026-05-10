# 🍳 Ślinotok — Django Recipe Book

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Modern-092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![Frontend](https://img.shields.io/badge/Frontend-HTML5_%26_CSS3-E34F26.svg?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web)

> A Django recipe catalog built without Bootstrap or JavaScript frameworks.
> Custom CSS Grid layout, category filtering, detailed recipe views and Django Admin — focused on backend fundamentals and clean frontend from scratch.

---

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Running Locally](#-running-locally)
- [What I Learned](#-what-i-learned)

---

## ✨ Features

- **Dynamic Recipe Catalog** — responsive grid layout displaying all available recipes
- **Category Filtering** — filter recipes by category (Main Courses, Desserts, Soups...) via custom URL routing and `.filter()` queries
- **Detailed Recipe Pages** — each recipe includes an image, preparation time, difficulty level, ingredients list and a short story behind the dish
- **Django Admin Panel** — full content management for recipes and categories out of the box
- **Custom Responsive UI** — built with HTML5 and CSS3 (Flexbox + CSS Grid), no Bootstrap, no JS frameworks

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Django |
| Frontend | HTML5, CSS3 (custom, no Bootstrap) |
| Database | SQLite |
| DevOps | Docker, Docker Compose |

---

## 📸 Screenshots

**Home Page**
![Home Page](docs/HomePAge.png)

**Recipe List**
![Recipe List](docs/List.png)

**Recipe Details**
![Recipe Details](docs/FoodDetails.png)

**About**
![About](docs/AboutMe.png)

---

## 📁 Project Structure

```text
django-recipe-book/
├── recipes/          # main app — models, views, URLs
├── slinotok/         # project config (settings, root URLs)
├── static/           # CSS, images
├── templates/        # HTML templates
├── manage.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 🚀 Running Locally

### Option 1: Docker (recommended)

```bash
git clone https://github.com/PiotrPliszka/django-recipe-book.git
cd django-recipe-book
docker compose up --build
```

App will be available at `http://localhost:8000`

### Option 2: Manual setup

```bash
git clone https://github.com/PiotrPliszka/django-recipe-book.git
cd django-recipe-book

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

App will be available at `http://localhost:8000`

---

## 🧠 What I Learned

- Structuring a Django project with models, views, URLs and templates
- Using `.filter()` for database queries and connecting them to URL parameters for category filtering
- Building database relations between models (recipes ↔ categories)
- Writing custom HTML/CSS layouts from scratch using CSS Grid and Flexbox
- Setting up Django Admin for content management without extra code
- Containerizing a Django app with Docker and Docker Compose

---

## 👤 Author

**Piotr Pliszka** — [GitHub](https://github.com/PiotrPliszka)
