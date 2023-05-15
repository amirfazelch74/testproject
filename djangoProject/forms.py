from django.contrib.auth import get_user_model
from django import forms



class ContactUsForm(forms.Form):
    fullName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )


class LoginForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter your passowrd'})
    )

User = get_user_model()

class Sms_login(forms.Form):
    phone=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your phonenumber'})
    )

class RegisterForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'})
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter your passowrd'})
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 're-enter your passowrd'})
    )

    def clean_userName(self):
        userName = self.cleaned_data.get('userName')
        query = User.objects.filter(username=userName)

        if query.exists():
            raise forms.ValidationError('this username is not available')
        return userName

    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email=email)

        if query.exists():
            raise forms.ValidationError('this email is already exist')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('passwords do not match')

        return data
