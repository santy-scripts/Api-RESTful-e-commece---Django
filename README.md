# Project Structure: `apiRest`

This project follows the standard Django architecture for building a RESTful API.
---

🧩 Structure
```
apiRest/
├── .vscode/ # Visual Studio Code settings
├── apiRest/ # Main Django project directory
│ ├── init.py
│ ├── asgi.py # ASGI configuration
│ ├── settings.py # Main project settings
│ ├── urls.py # Root URL configuration
│ └── wsgi.py # WSGI configuration
│
├── apps/ # Container folder for custom apps
│ └── apiApp/ # Main app (apiApp)
│ ├── init.py
│ ├── admin.py # Admin panel model registration
│ ├── apps.py # App configuration
│ ├── migrations/ # Database migration files
│ ├── models.py # ORM model definitions
│ ├── serializers.py # Serializers for Django REST Framework
│ ├── tests.py # Automated tests
│ ├── urls.py # App-specific URL configuration
│ └── views.py # View logic (controllers)
│
├── db.sqlite3 # Default SQLite database
├── manage.py # Django management script
└── venv/ # Python virtual environment

```
--- 

## Notes

- The main app is `apiApp`, located inside the `apps/` folder.
- It's recommended to place all new apps inside `apps/` for better organization.
- The `serializers.py` file is commonly used in Django REST Framework (DRF) projects.
- The default database is SQLite (`db.sqlite3`), but you can change it in `settings.py`.
