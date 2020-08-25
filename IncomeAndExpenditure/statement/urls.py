from django.urls import path
from . import views

urlpatterns = [
    path('IncomeExpenditure/', views.IncomeExpenditure, name='income-expenditure'),
    path('',views.statement, name='statement'),
]