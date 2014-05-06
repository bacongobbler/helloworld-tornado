helloworld-python
=================

a python hello world app using Tornado.

# Deployment

## Local

    $ pip install -r requirements.txt
    $ python app.py

## Deis

    $ deis create
    $ git push deis master

## Dokku

    $ git remote add dokku git@domain.com:helloworld-python
    $ git push dokku master

## Heroku

    $ heroku create
    $ git push heroku master
