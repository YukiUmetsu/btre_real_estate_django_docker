from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    result = validate_new_user(request)
    if result['errors']:
        messages.error(request, result['errors'][0])
        return redirect('register')

    rawUser = result['user']
    user = User.objects.create_user(
        username=rawUser['username'],
        password=rawUser['password'],
        email=rawUser['email'],
        first_name=rawUser['first_name'],
        last_name=rawUser['last_name'])
    user.save()
    auth.login(request, user)
    messages.success(request, 'You are now logged in!')
    return redirect('index')


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    user = validate_user(request)

    if not user:
        messages.error(request, 'Invalid Credentials')
        return render(request, 'accounts/login.html')

    auth.login(request, user)
    messages.success(request, 'You are now logged in!')
    return redirect('dashboard')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out!')
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def validate_new_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    user = {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'email': email,
        'password': password,
        'password2': password2,
    }
    errors = []

    if password != password2:
        errors.append('Passwords do not match')
        return {'errors': errors}

    if User.objects.filter(username=username).exists():
        errors.append('That username is taken')
        return {'errors': errors}

    if User.objects.filter(email=email).exists():
        errors.append('That email is already registered')
        return {'errors': errors}

    return {'user': user, 'errors': []}


def validate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is None:
        return False

    return user
