from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm
from .models import MyUserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            myuser = MyUserProfile()
            myuser.first_name = form.cleaned_data.get('first_name')
            myuser.last_name = form.cleaned_data.get('last_name')
            myuser.date_of_birth = form.cleaned_data.get('date_of_birth')
            myuser.username = form.cleaned_data.get('username')
            # myuser.date_of_birth = form.cleaned_data.get('date_of_birth')
            # myuser.first_name = form.cleaned_data.get('username')
            # myuser.date_of_birth = form.cleaned_data.get('date_of_birth')
            myuser.save()
            form.save()
            messages.success(request, f'Your account has been created! You are now able to login as')
            return redirect('frontend-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    return render(request,'users/login.html')
