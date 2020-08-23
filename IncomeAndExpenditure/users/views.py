from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm
from .models import MyUserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            myuser = MyUserProfile()
            myuser.first_name = form.cleaned_data.get('first_name')
            myuser.last_name = form.cleaned_data.get('last_name')
            myuser.email = form.cleaned_data.get('email')
            myuser.phone_number = form.cleaned_data.get('phone_number')
            myuser.date_of_birth = form.cleaned_data.get('date_of_birth')
            myuser.address_line_1 = form.cleaned_data.get('address_line_1')
            myuser.address_line_2 = form.cleaned_data.get('address_line_2')
            myuser.city = form.cleaned_data.get('city')
            myuser.postcode = form.cleaned_data.get('postcode')
            myuser.username = form.cleaned_data.get('username')
            
            myuser.save()
            form.save()
            messages.success(request, f'Your account has been created! You are now able to login as')
            return redirect('frontend-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
