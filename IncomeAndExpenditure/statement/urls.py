from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('IncomeExpenditure/', views.IncomeExpenditure, name='income-expenditure'),
    path('',views.statement,name='statement'),
]