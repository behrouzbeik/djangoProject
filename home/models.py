from django.db import models

# Create your models here.

class MenuItems(models.Model):
    EnCaption = models.CharField(max_length=50)
    DeCaption = models.CharField(max_length=50)
    Url = models.CharField(max_length=100)

    def __str__(self):
        return self.EnCaption