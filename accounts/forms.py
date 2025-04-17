from django import forms
from .models import Account

class RegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="تایید رمز عبور")

    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تماس',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("رمز عبور و تایید آن مطابقت ندارند.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200, label="ایمیل")
    password = forms.CharField(widget=forms.PasswordInput(), label="رمز عبور")

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'uni_name', 'facility_name']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'uni_name': 'نام دانشگاه',
            'facility_name': 'نام دانشکده'
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Account.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت شده است.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if Account.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError('این نام کاربری قبلاً ثبت شده است.')
        return username
