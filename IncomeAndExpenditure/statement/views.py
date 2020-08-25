from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .form import IncomeExpenditureForm
from .models import IncomeExpenditureStatement

@login_required
def IncomeExpenditure(request):
   if request.method == 'POST':
      statementform = IncomeExpenditureForm(request.POST)
      if statementform.is_valid():
         statementform.save()
         #IncomeExpenditureStatement.objects.filter(author=request.user).author = request.user
         #IncomeExpenditureStatement.objects.filter(author=request.user).author_id = request.user.id
         # statement = IncomeExpenditureStatement()
         # statement.salary = statementform.cleaned_data.get('salary')
         # statement.other = statementform.cleaned_data.get('other')
         # statement.mortgage = statementform.cleaned_data.get('mortgage')
         # statement.rent = statementform.cleaned_data.get('rent')
         # statement.utilities = statementform.cleaned_data.get('utilities')
         # statement.travel = statementform.cleaned_data.get('travel')
         # statement.food = statementform.cleaned_data.get('food')
         # statement.loans = statementform.cleaned_data.get('loans')
         # statement.credit_cards = statementform.cleaned_data.get('credit_cards')
         messages.success(request, f'Your income and expenditure have been recorded! You can view it by clicking on the statement button.')
         return redirect('statement')
   else:
      statementform = IncomeExpenditureForm()
   return render(request,'statement/IncomeExpenditure.html',{'statementform': statementform})

@login_required
def statement(request):
   return render(request,'statement/main.html')