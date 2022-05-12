from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.username
