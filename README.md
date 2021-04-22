# Back Office Bateau Thibault (Django)

## Virtual environnement

Create a virtual environnement and activate it:

- Linux

    ```
    python -m venv env
    source env/bin/activate
    ```

- Windows 10

    ```
    python -m venv env
    .\env\Scripts\activate
    ```

## Dependencies

Install dependencies :

- Linux

    ```
    pip install django djangorestframework requests django-cors-headers pandas djangorestframework-simplejwt
    ```

- Windows 10

    ```
    pip install django djangorestframework requests django-cors-headers pandas djangorestframework-simplejwt
    ```

## Load database 


- Linux and windows 10

    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py refresh
    python manage.py reset_transactions
    ```

## Create user

To access the web-app features, you need a user account.

- Linux and Windows 10

    ```
    python manage.py createsuperuser
    ```

Here is an exemple :

```
username : admin
email    : admin@admin.com
password : admin
byPass?  : Yolo
```

## Launch Web-service

- Linux and Windows 10

    ```
    python manage.py runserver
    ```
