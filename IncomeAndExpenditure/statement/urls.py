from django.urls import path
#from .views import StatementCreateView, StatementUpdateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('IncomeExpenditure/', views.IncomeExpenditure, name='income-expenditure'),
    #path('IncomeExpenditure/',login_required(StatementCreateView.as_view()),name='income-expenditure'),
    #path('IncomeExpenditure/update',login_required(StatementUpdateView.as_view()),name='update-income-expenditure'),
    path('',views.statement,name='statement'),
]