from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .form import UserRegisterForm
from .models import MyUserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.filter(username=form.cleaned_data.get("username")).first()
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
            myuser.author = user
            messages.success(request, f'Your account has been created! You are now able to login as {myuser.username}')
            myuser.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    username = MyUserProfile.objects.filter(username=user).first().username
    first_name = MyUserProfile.objects.filter(username=user).first().first_name
    last_name = MyUserProfile.objects.filter(username=user).first().last_name
    email = MyUserProfile.objects.filter(username=user).first().email
    phone_number = MyUserProfile.objects.filter(username=user).first().phone_number
    date_of_birth = MyUserProfile.objects.filter(username=user).first().date_of_birth
    address_line_1 = MyUserProfile.objects.filter(username=user).first().address_line_1
    address_line_2 = MyUserProfile.objects.filter(username=user).first().address_line_2
    city = MyUserProfile.objects.filter(username=user).first().city
    postcode = MyUserProfile.objects.filter(username=user).first().postcode
    
    context={
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone_number': phone_number,
        'date_of_birth': date_of_birth,
        'address_line_1': address_line_1,
        'address_line_2': address_line_2,
        'city': city,
        'postcode': postcode
    }
    return render(request, 'users/profile.html',context)
