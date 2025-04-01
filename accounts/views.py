from django.shortcuts import render, redirect
from .forms import RegisterationForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'با موفقیت ثبت نام شدید و وارد حساب کاربری خود شدید!')
            return redirect('home')
        else:
            messages.error(request, 'ثبت نام ناموفق. لطفاً اطلاعات را بررسی کنید.')
    else:
        form = RegisterationForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):  
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                auth_login(request, user)  
                return redirect('home') 
            else:
                messages.error(request, "اطلاعات وارد شده صحیح نیست!") 
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home')


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        messages.success(self.request, "رمز عبور شما با موفقیت تغییر کرد.")
        return super().form_valid(form)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات شما با موفقیت به‌روزرسانی شد.')
            return redirect('edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})
