from django import forms
from django.contrib.auth.models import User
from .models import IncomeExpenditureStatement

class IncomeExpenditureForm(forms.ModelForm):
    class Meta:
        model = IncomeExpenditureStatement
        fields = ['salary','other','mortgage','rent','utilities','travel','food','loans','credit_cards']