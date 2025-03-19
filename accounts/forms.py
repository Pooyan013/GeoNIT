from django import forms
from .models import Account

class RegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'رمز عبور را وارد کنید'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'رمز عبور را دوباره وارد کنید'
    }))
    
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "email", "username", "password", "confirm_password", "uni_name", "facility_name"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("رمز عبور و تأیید رمز عبور باید یکسان باشند.")
        
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
