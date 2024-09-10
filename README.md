# Django Todo App

A simple yet powerful Todo app built with Django. This app allows users to create, update, and delete tasks with ease.

### Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [App URL](#app-url)
- [Admin Access](#admin-access)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

## Features
- **Add Todo**: Create a new task with a title and description.
- **Update Todo**: Modify existing tasks (title, description, or mark them as completed).
- **Delete Todo**: Remove tasks from the list.
- **Mark as Complete**: Quickly mark tasks as completed or uncompleted.
- **Simple UI**: A minimalist interface built using Bootstrap for ease of use.
  
## Setup

### Prerequisites
- Python 3.x installed on your machine.
- Django framework installed. If Django is not installed, follow [this guide](https://www.djangoproject.com/download/) to install it.

### Step 1: Clone the Repository
Clone the repository to your local machine.

```bash
$ git clone https://github.com/abhishekdubey369/todo-django.git
$ cd django-todo
```

### Step 2: Install Required Dependencies
To install Django and other required dependencies, run:

```bash
$ pip install -r requirements.txt
```

This will install Django and any other packages the project needs.

### Step 3: Migrations

Create all the migration files necessary for setting up the database:

```bash
$ python manage.py makemigrations
```

Now, apply the migrations to create the database schema:

```bash
$ python manage.py migrate
```

### Step 4: Create a Superuser

To access the Django admin panel, create a superuser by running the following command. You'll be prompted to provide a username, password, and email address:

```bash
$ python manage.py createsuperuser
```

### Step 5: Start the Development Server

To start the app on your local machine, run the Django development server:

```bash
$ python manage.py runserver
```

### Step 6: Access the App

Once the server is running, open your web browser and navigate to:

```bash
http://127.0.0.1:8000/todos
```

You should now see the Todo App in action.

## Running the Application

### Access the Admin Panel
To manage tasks or users from the Django admin panel, visit the admin panel at:

```bash
http://127.0.0.1:8000/admin
```

Log in using the credentials you set up in the `createsuperuser` step.

### App URL
To access the Todo app directly:

```bash
http://127.0.0.1:8000/todos
```

### Admin Access
The Django admin panel can be accessed by visiting:

```bash
http://127.0.0.1:8000/admin
```

Use the credentials from the `createsuperuser` command to log in.

## Troubleshooting

- **Database errors**: If you encounter database errors or missing migrations, ensure that you've run `python manage.py migrate` correctly.
- **Static files not loading**: If static files like CSS or JS aren't loading, ensure `DEBUG = True` in `settings.py` during development.
- **Server not starting**: Ensure Django is installed and properly configured by running `pip install -r requirements.txt` and retrying.

## Future Enhancements

- **User Authentication**: Add user registration and login functionality.
- **Due Dates**: Allow users to assign due dates to tasks.
- **Task Categories**: Group tasks under customizable categories.
- **Search Functionality**: Add a search feature to easily find tasks.

Cheers and Happy Coding! 🎉