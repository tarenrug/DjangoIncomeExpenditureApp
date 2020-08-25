from django.db import models
from django.contrib.auth.models import User

class MyUserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    date_of_birth = models.DateField()
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.username
