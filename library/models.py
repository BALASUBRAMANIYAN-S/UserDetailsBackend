from django.db import models


class books(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
 