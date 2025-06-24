# tasktodo-task-manager

This is a simple task manager web app built with Python using Django framework. This app 
allows users create, update, delete and assign workers to each task which will help them organize their work.

## Installation 

Python3 must be already installed
```shell
git clone https://github.com/rkostiv253/tasktodo-task-manager.git
cd tasktodo_task_manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
```
## Features

- Create, delete and edit tasks, task types, workers and their position
- Assign workers and logged-in user to task
- Set deadlines for tasks and mark them complete
- Search tasks, task types, workers and positions

## Tech stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (Bootstrap4)
- **Database**: SQLite

## Project structure

tasktodo_task_manager:
├── static
│   └── assets
│       └── css
│       └── fonts
│       └── img
│       └── js
│       └── scss
├── task_manager
│   ├── __init__.py
│   ├── asgi.py.
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasktodo
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── templates
    ├── includes
    ├── layouts
    ├── registration
    └── tasktodo
├── .env
├── .env.sample
├── .flake8
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
