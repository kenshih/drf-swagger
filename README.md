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
```

# setup

random tutorial: 
* https://builtwithdjango.com/blog/basic-django-setup
* https://medium.com/django-pycharm-integration/how-to-create-a-simple-rest-api-with-django-ec9829fd5415