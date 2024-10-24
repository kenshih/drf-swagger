# drf-swagger

An experiment running drf-yasg & drf-spectacular on Django 4.2, to see how they play together.

The purpose of this it to plan a transition from yasg to spectacular, with minimal disruption, allowing for a gradual cutover and ability to preview changes in various environments before doing the whole cutover.


# run project
```
poetry run python manage.py runserver
```

# client when server is running

```
curl http://127.0.0.1:8000/api

curl -X POST http://127.0.0.1:8000/api/ \
     -H "Content-Type: application/json" \
     --data '{ "title":"My Life as a Guinea Pig, the Sequel", "year_published": 2024 }'

# alternatively...
brew install hurl
hurl hurl/get.hurl
hurl hurl/post.hurl # this creates a record, not idempotently, so you'll get duplicates when running again
hurl hurl/schema-spectacular.hurl
hurl hurl/schema-yasg.hurl
```
# Urls of swagger-land

drf-spectacular
- http://127.0.0.1:8000/api/schema/ - triggers download of yaml when in browser
- http://127.0.0.1:8000/api/schema/swagger-ui/
- http://127.0.0.1:8000/api/schema/redoc/

drf-yasg
- http://127.0.0.1:8000/api/swagger/
- http://127.0.0.1:8000/api/swagger.json/
- http://127.0.0.1:8000/api/swagger.yaml/ - triggers download of yaml when in browser
- http://127.0.0.1:8000/api/redoc/

# setup

random tutorial: 
* https://builtwithdjango.com/blog/basic-django-setup
* https://medium.com/django-pycharm-integration/how-to-create-a-simple-rest-api-with-django-ec9829fd5415

yasg: https://drf-yasg.readthedocs.io/en/stable/readme.html#usage

random gotchas
```
# for yasg, needed
poetry add setuptools
```