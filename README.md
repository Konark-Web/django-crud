## Django CRUD project
This is a simple sample project to show your skills with basic Django functionality.
I used Bootstrap as the markup and styles.

### How install:
1. Install all libs from requirements.txt:
```pip3 install -r requirements.txt```
2. Create new database: ```CREATE DATABASE djangocrud;```
3. Create new user: ```CREATE USER 'django-crud'@'localhost' IDENTIFIED BY '123456qQ';```
4. Give privileges to the user: ```GRANT ALL PRIVILEGES ON djangocrud.* TO 'django-crud'@'localhost';```
5. Run migration: ```python manage.py migrate```
6. Run django server: ```python manage.py runserver```
7. Now you can create superuser: ```python manage.py createsuperuser``` (or signup on website: /signup/)


### Features:
- Login, logout, signup
- Create new post
- Edit current post
- Delete post
- List of posts, single post
- View counter (without IP/cookie/session checker)

#### Screenshots:
https://imgur.com/a/9khJpaN