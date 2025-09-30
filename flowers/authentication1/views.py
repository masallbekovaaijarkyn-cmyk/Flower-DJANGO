from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Profile

def home_view(request):
    # Выход
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('home')

    # Регистрация
    if request.method == 'POST' and 'signup' in request.POST:
        signup_form = SignUpForm(request.POST)
        login_form = AuthenticationForm()
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.set_password(signup_form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        signup_form = SignUpForm()

    # Вход
    if request.method == 'POST' and 'login' in request.POST:
        login_form = AuthenticationForm(data=request.POST)
        signup_form = SignUpForm()
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
    else:
        login_form = AuthenticationForm()

    # Если пользователь вошёл → показать профиль
    if request.user.is_authenticated:
        return render(request, 'authentication/home.html', {'user': request.user})

    # Если не вошёл → показать обе формы
    return render(request, 'authentication/home.html', {
        'signup_form': signup_form,
        'login_form': login_form,
    })
