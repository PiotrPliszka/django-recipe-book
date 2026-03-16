# 🍳 Ślinotok - Django Recipe Book

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Modern-092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![HTML5 & CSS3](https://img.shields.io/badge/Frontend-HTML5_&_CSS3-E34F26.svg?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web)

> A modern, responsive web application for managing and displaying culinary recipes. This project was built to showcase core Django functionalities, database relations, and clean front-end design without the use of heavy JavaScript frameworks.

---

## 📑 Table of Contents
- [✨ Features](#-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [🚀 How to run this project](#-how-to-run-this-project)
  - [Option 1: Using Docker (Recommended)](#option-1-using-docker-recommended)
  - [Option 2: Local Setup (without Docker)](#option-2-local-setup-without-docker)
- [📸 Screenshots](#-screenshots)
- [🤝 Author](#-author)

---

## ✨ Features

* **🍽️ Dynamic Recipe Catalog:** A visually appealing grid layout displaying all available recipes.
* **🔍 Category Filtering:** Users can filter recipes by categories (e.g., Main Courses, Desserts, Soups) using custom URL routing and database queries (`.filter()`).
* **📖 Detailed Recipe Pages:** Dedicated views for each recipe including an image, preparation time, difficulty level, ingredients list, and the story behind the dish.
* **⚙️ Admin Dashboard:** Fully integrated Django Admin panel for easy content management (adding/editing recipes and categories).
* **📱 Responsive UI:** Custom front-end built with HTML5 and CSS3 (Flexbox & CSS Grid) ensuring the app looks great on both desktop and mobile devices.

---

## 🛠️ Technologies Used

**Backend:**
* Python 3
* Django

**Frontend:**
* HTML5, CSS3 (Custom design, no Bootstrap)

**Database & DevOps:**
* SQLite (default Django DB)
* Docker & Docker Compose

---

## 🚀 How to run this project

First, clone the repository to your local machine:

```bash
git clone [https://github.com/PiotrPliszka/django-recipe-book.git](https://github.com/PiotrPliszka/django-recipe-book.git)
cd django-recipe-book
