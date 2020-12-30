from django.db import models

class Sweet(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name