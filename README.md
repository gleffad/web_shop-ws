# Back Office Bateau Thibault (Django)

## Environement virtuel

Créer un environnement virtuel pour installer les dépendances et l'activer:

- Sur linux

    ```
    python3 -m venv env
    source env/bin/activate
    ```

- Sur Windows 10

    ```
    python -m venv env
    .\env\Scripts\activate
    ```

## Installation des dépendances

Ce mettre dans l'environement de travail et installer les depandance suivantes :

- Sur linux

    ```
    pip3 install django djangorestframework requests django-cors-headers pandas djangorestframework-simplejwt
    ```

- Sur Windows 10

    ```
    pip install django djangorestframework requests django-cors-headers pandas djangorestframework-simplejwt
    ```

## Chargement de la base de donnée

Une fois les dépandances installer, mettre a jour la base de donnée.

- Sur linux

    ```
    python3 manage.py migrate
    python3 manage.py refresh
    python3 manage.py reset_transactions
    ```

- Sur Windows 10

    ```
    python manage.py migrate
    python manage.py refresh
    python manage.py reset_transactions
    ```

## Création de l'utilisateur

Pour accéder au site il faudra vous créer un utilisateur.

- Sur linux

    ```
    python3 manage.py createsuperuser
    ```

- Sur Windows 10

    ```
    python manage.py createsuperuser
    ```

Voici un exemplete d'utilisateur que vous pouriez crée

```
username : admin
email    : admin@admin.com
password : admin
byPass?  : Y
```

## Lancer le serveur 

- Sur linux

    ```
    python3 manage.py runserver
    ```

- Sur Windows 10

    ```
    python manage.py runserver
    ```



