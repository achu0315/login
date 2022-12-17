from django.db import models


# Create your models here.


class Form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

