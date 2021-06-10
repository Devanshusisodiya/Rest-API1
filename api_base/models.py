from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=90)
    superpower = models.CharField(max_length=90)

    def __str__(self):
        return self.name