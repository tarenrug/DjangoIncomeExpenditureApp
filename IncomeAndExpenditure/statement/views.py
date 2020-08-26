from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from .form import IncomeExpenditureForm
from .models import IncomeExpenditureStatement
from .FunctionScript import IEFunction

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
         messages.success(request, f'Your income and expenditure have been recorded! You can edit this by clicking on the Register Statement button.')
         return redirect('statement')
   else:
      try:
         current_data = IncomeExpenditureStatement.objects.filter(author=request.user).first()
         statementform = IncomeExpenditureForm(initial={'salary': current_data.salary,'other': current_data.other,'mortgage': current_data.mortgage,
         'rent': current_data.rent,'utilities': current_data.utilities,'travel': current_data.travel,'food': current_data.food,'loans': current_data.loans,
         'credit_cards': current_data.credit_cards})
      except AttributeError:
         current_data={}
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

   return render(request,'statement/IncomeExpenditure.html',{'statementform': statementform,'form1':form1,'form2':form2,'current_data': current_data})

@login_required
def statement(request):
   try:
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
   except AttributeError:
      return render(request,'statement/main2.html')


# Attempt with Class Based view

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


