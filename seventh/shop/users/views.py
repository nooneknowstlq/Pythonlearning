from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()

    content = {'title': 'Авторизация',
               'form': form
               }
    return render(request, 'users/login.html', content)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    content = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', content)


def profile(request):
    form = UserProfileForm(instance=request.user)


    context = {
        'title': 'Store - профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)
