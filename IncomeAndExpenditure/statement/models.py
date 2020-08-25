from django.db import models
from django.contrib.auth.models import User

class IncomeExpenditureStatement(models.Model):
    salary = models.IntegerField
    other = models.IntegerField
    mortgage = models.IntegerField
    rent = models.IntegerField
    utilites = models.IntegerField
    travel = models.IntegerField
    food = models.IntegerField
    loans = models.IntegerField
    credit_cards = models.IntegerField
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username