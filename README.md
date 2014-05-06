helloworld-python
=================

a python hello world app using Tornado.

# Deployment

## Deis

    $ deis create
    $ git push deis master

## Dokku

    $ git remote add dokku git@domain.com:helloworld-python
    $ git push dokku master

## Heroku

    $ heroku create
    $ git push heroku master
