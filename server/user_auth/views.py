from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("email,password", email, password)

        user = authenticate(request, username=email, password=password)
        print("user",user)
        if user is not None:
            login(request, user)
            return render(request, 'authentication/dashboard.html')  
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid credentials'})


    return render(request, 'authentication/login.html')


def sign_user(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')  # optional if not saved in default User model
        if User.objects.filter(username=username).exists():
            context['error'] = "Username already taken"
        elif User.objects.filter(email=email).exists():
            context['error'] = "Email already registered"
        else :
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()


    return render(request, 'authentication/sign.html')

