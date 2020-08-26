from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=14)
    date_of_birth = forms.DateField(label="Date of Birth (DD/MM/YYYY)",input_formats=['%d/%m/%Y'])
    address_line_1 = forms.CharField(max_length=100)
    address_line_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone_number','date_of_birth','address_line_1','address_line_2','city','postcode','username', 'password1', 'password2']