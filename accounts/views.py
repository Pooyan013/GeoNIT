from django.shortcuts import render, redirect
from .forms import RegisterationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user) 
                return redirect('home')  
            else:
                messages.error(request, "اطلاعات وارد شده صحیح نیست!") 
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})
