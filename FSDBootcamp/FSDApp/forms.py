from django import forms
from django.forms import ModelForm
from FSDApp.models import registeredUser


class registeredUser(ModelForm):
    class Meta:
        model = registeredUser
        fields = '__all__'

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}) )
    last_name = forms.CharField(label="Last name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    your_contact = forms.CharField(label="Contact", max_length=15, widget=forms.TextInput(attrs={'type': 'tel','class': 'form-control'}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))