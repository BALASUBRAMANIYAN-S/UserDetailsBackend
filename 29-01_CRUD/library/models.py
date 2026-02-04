from django.db import models


class books(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
 