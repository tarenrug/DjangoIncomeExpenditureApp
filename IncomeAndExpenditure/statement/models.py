from django.db import models
from django.contrib.auth.models import User

class IncomeExpenditureStatement(models.Model):
    salary = models.IntegerField(default=0)
    other = models.IntegerField(default=0)
    mortgage = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)
    utilites = models.IntegerField(default=0)
    travel = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    loans = models.IntegerField(default=0)
    credit_cards = models.IntegerField(default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username