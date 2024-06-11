# E-commerce Backend Service

This is the backend service for an e-commerce website, built with Django. It provides APIs for managing products, categories, regions, carts, and stock.

## Table of Contents

- [Installation](#installation)
- [Running Locally](#running-locally)
- [Setting Up PostgreSQL on Render](#setting-up-postgresql-on-render)
- [Deploying on Render](#deploying-on-render)
- [Creating Superuser and accesing Django Admin](#viewing-database-enteries-on-django-admin)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/WSAbackend.git
    cd WSAbackend
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv env
    cd env/Scripts
    activate
    cd ../..
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Running Locally

1. **Navigate to the project directory:**

    ```sh
    cd WSAbackend
    ```

2. **Apply the migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

3. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000`.

## Setting Up PostgreSQL on Render

1. **Create a PostgreSQL Database on Render:**
   - Go to your Render dashboard.
   - Click on `New` and select `Database`.
   - Choose `PostgreSQL` and configure the database (name, region, etc.).
   - Once created, note the database URL provided by Render.

2. **Update Django Settings:**
   - In your `settings.py` file, in the WSAbackend directory update the `DATABASES` setting to use the PostgreSQL database URL. Replace `your_database_url` with the URL from Render:


    ```python
    import os
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.parse('your_database_url')
    }
    ```

3. **Apply Migrations Before Deployment:**
   - Ensure you apply migrations to your PostgreSQL database before deployment:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

## Deploying on Render

To deploy the application on [Render](https://render.com/), follow these steps:

1. **Create a New Web Service on Render:**
   - Go to your Render dashboard.
   - Click on `New` and select `Web Service`.
   - Connect your GitHub or GitLab account and select the repository for the project.

2. **Configure the Web Service:**
   - **Environment**: Select `Python 3`.
   - **src**: 
    ```sh
        cd WSAbackend
     ```
   - **Build Command**: Set this to `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`. (There touch this part on render. Leave it as it is)
   - **Start Command**: Set this to `gunicorn WSAbackend.wsgi:application`.

3. **Deploy the Web Service:**
   - Click `Create Web Service` to deploy your application.
   - Render will build and deploy your application. Once the deployment is complete, your application will be available at the URL provided by Render.

## Viewing Database Enteries on Django Admin
    
    To view the database follow the following commands
1. **Create Superuser:**
    - run
        ```sh
        python manage.py createsuper

        ```
    - After following the prompts and creating the user, visit `http://hosted_url/admin.com`.
    - Fill in the credentials used previously