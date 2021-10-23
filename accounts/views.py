# Django
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# local Django

from .models import User, UserManager, Profile
# from .tokens import account_activation_token

# Create your views here.

@login_required
def home(request):
    return render(request , 'home/index.html')

def login_page(request):

    if request.method == 'POST':
        if request.POST.get('submit') == 'login':
            email = request.POST['email']
            password1 = request.POST['password1']
            user = authenticate(email=email, password1=password1)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("patients:patient_login")
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("patients:patient_login")


        if request.POST.get('submit') == 'sign_up':
            email = request.POST['email']
            name = request.POST['name']
            phone = request.POST['phone']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            if (password1!= password2):
                messages.error(request, " Passwords do not match")
                return redirect('accounts:login_page')
        
            # Create the user
            user = User.objects.filter(email=email)
            user = User(email=email,name=name, phone=phone, is_active=False)
            user.set_password(password1) # To save password as hash
            user.save()
            messages.success(request, " Your meetMyDoctor has been successfully created")
            return redirect('accounts:login_page')

    return render(request, 'accounts/login.html')


def signup_success(request):
    return render(request,'accounts/signup_success.html')

def account_authenticated(request):
    return render(request, 'accounts/account_authenticated')