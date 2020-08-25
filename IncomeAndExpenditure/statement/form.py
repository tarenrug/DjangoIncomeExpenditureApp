from django import forms
from django.contrib.auth.models import User
from .models import IncomeExpenditureStatement

class IncomeExpenditureForm(forms.ModelForm):
    salary = forms.IntegerField(max_value=1000000000000)
    other = forms.IntegerField(max_value=1000000000000)
    mortgage = forms.IntegerField(max_value=1000000000000)
    rent = forms.IntegerField(max_value=1000000000000)
    utilites = forms.IntegerField(max_value=1000000000000)
    travel = forms.IntegerField(max_value=1000000000000)
    food = forms.IntegerField(max_value=1000000000000)
    loans = forms.IntegerField(max_value=1000000000000)
    credit_cards = forms.IntegerField(max_value=1000000000000)
    class Meta:
        model = IncomeExpenditureStatement
        fields = ['salary','other','mortgage','rent','utilites','travel','food','loans','credit_cards']