<div align="center">

# Task Manager

A simple and flexible task management web application

[![Actions Status](https://github.com/tanuki-evil1/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tanuki-evil1/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3b8d2ae4582e40fef37b/maintainability)](https://codeclimate.com/github/tanuki-evil1/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3b8d2ae4582e40fef37b/test_coverage)](https://codeclimate.com/github/tanuki-evil1/python-project-52/test_coverage)

</div>

## About

A task management web application built with Python and [Django](https://www.djangoproject.com/) framework. It allows
you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with
the system.

To provide users with a convenient, adaptive, modern interface, the project uses
the [Bootstrap](https://getbootstrap.com/) framework.

The frontend is rendered on the backend. This means that the page is built by the DjangoTemplates backend, which returns
prepared HTML. And this HTML is rendered by the server.

[PostgreSQL](https://www.postgresql.org/) is used as the object-relational database system.

#### --> [Demo](https://task-manager-xggd.onrender.com) <--

### Stack

* Python
* Django
* Bootstrap 5
* PostgreSQL
* Poetry
* Gunicorn
* Whitenoise
* Rollbar
* Flake8

## Usage and Installation

```bash
git clone https://github.com/tanuki-evil1/Task-Manager.git
cd Task-Manager

## Configuration
Before running the application, you need to set up your environment variables. Duplicate the `.env.example` file and
rename it to `.env`. Then, modify it with your actual data for the following variables:

- `SECRET_KEY`: a secret key for your application.
- `DATABASE_URL`: the connection string for your PostgreSQL database, formatted
  as `postgresql://username:password@localhost:5432/database_name`.

# Install dependencies
make install

# Migrate
make migrate

# Run the local development server (make start - production server)
make dev
```
