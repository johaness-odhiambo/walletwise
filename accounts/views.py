from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout



# Create your views here.
def register(request):
    if request.method == 'POST':
      name = request.POST['name']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      confirm_password = request.POST['confirm'] 

      # To check if password match 
      if password == confirm_password:
         if User.objects.filter(username=username). exists():
            messages.error(request, 'Username already exists')

         elif User.objects.filter(email=email). exists():
            messages.error(request,'Email already exists')
         else:
            user= User.objects.create_user( username=username, email=email, password=password) 
            user.save()
            messages.success(request, 'You are successfully registered')
            return redirect('accounts:login')
      else:
         messages.error(request, 'password do not match')
    context = {
       'values': request.POST
    }
    return render(request, 'authentication/register.html')
# login function
def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)
       
        if user is not None: 
            auth_login(request, user) 
            messages.success(request, 'You are now logged in') 
            return redirect('dashboard:dashboard')
    
        else: messages.error(request, 'Invalid credentials')
    context = { 
    'values': request.POST
        } 
    return render(request, 'authentication/login.html', context)

# logout    
def logout(request):
   auth_logout(request)
   messages.success(request, 'You  are logged out')
   return redirect('accounts:login')
   

