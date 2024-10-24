from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=100)
    year_published = models.PositiveSmallIntegerField()

class Worklist(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)