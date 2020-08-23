from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import IncomeForm

@login_required
def income(request):
    render(request,'statement/income.html',{'IncomeForm': IncomeForm})
