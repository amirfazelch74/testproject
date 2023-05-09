from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .forms import ContactUsForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'message': 'Hi, welcome to my project'
    }
    return render(request, 'home_page.html', context)


def about_us_page(request):
    context = {
        'message': 'Hiiiiiiiiiiiiiiiiiiiiiiiii',
        'about_text': 'hi, this is about page, this text from about us function'
    }
    return render(request, 'about_us_page.html', context)


def contact_us_page(request):
    contact_form = ContactUsForm()
    if request.method == "POST":
        print(request.POST.get('fullName'))
        print(request.POST.get('email'))
        print(request.POST.get('message'))

    context = {
        'contact_text': 'hi, this is about page, this text from about us function',
        'contact_form': contact_form
    }
    return render(request, 'contact_us_page.html', context)


def login_page(request):
    print(request.user.is_authenticated)
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        userName = login_form.cleaned_data.get('userName')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')

    context = {
        'message': 'Login Page',
        'login_form': login_form
    }
    return render(request, 'login.html', context)


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        userName = register_form.cleaned_data.get('userName')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        new_user = User.objects.create_user(username=userName, email=email, password=password)
        print(new_user)

    context = {
        'title': 'Register Page',
        'message': 'Register Form',
        'register_form': register_form
    }
    return render(request, 'register.html', context)


def log_out(request):
    logout(request)
    return redirect('/')
