from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from .form import IncomeExpenditureForm
from .models import IncomeExpenditureStatement
from .FunctionScript import IEFunction

# class StatementCreateView(CreateView):
#    model = IncomeExpenditureStatement
#    template_name='statement/IncomeExpenditure.html'
#    form_class = IncomeExpenditureForm
#    fields = ['salary','other']

#    def form_valid(self, form):
#       object = form.save(commit=False)
#       object.author = self.request.user
#       form.save()
#       return super(StatementCreateView, self).form_valid(form)

#    def get(self, request):
#       statementform = self.form_class(initial=self.initial)
#       return render(request, self.template_name, {'statementform': statementform})

#    def post(self, request):
#       statementform = self.form_class(request.POST)
#       if statementform.is_valid():
#          statementform.save()
#          messages.success(request, f'Your income and expenditure have been recorded! You can view it by clicking on the statement button.')
#          return redirect('statement')

#       return render(request, self.template_name, {'statementform': statementform})

# class StatementUpdateView(UpdateView):
#    model = IncomeExpenditureStatement
#    template_name='statement/IncomeExpenditure.html'
#    form_class = IncomeExpenditureForm
#    fields=['salary','other','mortgage','rent','utilites','travel','food','loans','credit_cards']

#    def form_valid(self, form):
#       form.instance.author = self.request.user
#       return super().form_valid(form)


@login_required
def IncomeExpenditure(request):
   if request.method == 'POST':
      try:
         I = IncomeExpenditureStatement.objects.get(author=request.user)
         statementform = IncomeExpenditureForm(request.POST,instance=I)
      except IncomeExpenditureStatement.DoesNotExist:
         statementform = IncomeExpenditureForm(request.POST)
      statementform.instance.author=request.user
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
         messages.success(request, f'Your income and expenditure have been recorded! You edit this by clicking on the Register Statement button.')
         return redirect('statement')
   else:
      statementform = IncomeExpenditureForm()

   form1=[]
   form2=[]
   count=0
   for i in statementform:
      count+=1
      if count<=2:
         form1.append(i)
      else:
         form2.append(i)

   return render(request,'statement/IncomeExpenditure.html',{'statementform': statementform,'form1':form1,'form2':form2})

@login_required
def statement(request):
   CurrentStatement=IncomeExpenditureStatement.objects.filter(author=request.user).first()
   salary = CurrentStatement.salary
   other = CurrentStatement.other
   mortgage = CurrentStatement.mortgage
   rent = CurrentStatement.rent
   utilities = CurrentStatement.utilities
   travel = CurrentStatement.travel
   food = CurrentStatement.food
   loans = CurrentStatement.loans
   credit_cards = CurrentStatement.credit_cards

   (Income,Expenditure,Disposible,IERating,Grade)=IEFunction([salary,other],[mortgage,rent,utilities,travel,food,loans,credit_cards])

   context={'salary': salary,
            'other': other,
            'mortgage': mortgage,
            'rent': rent,
            'utilities': utilities,
            'travel': travel,
            'food': food,
            'loans': loans,
            'credit_cards': credit_cards,
            'Income': Income,
            'Expenditure': Expenditure,
            'Disposible': Disposible,
            'IERating': IERating,
            'Grade': Grade
   }
   return render(request,'statement/main.html',context)

