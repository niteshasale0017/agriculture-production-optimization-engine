from django import forms
from .models import User
from django.core import validators
from django.forms import ModelForm

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'fullname':'Full Name',
            'email':'Email',
            'mobile':'Mobile',
            'password':'Password'
        }
        widgets = {
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Full Name','autocomplete':'off'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'@mail.com','autocomplete':'off'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'91+ 0000000000','autocomplete':'off'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','autocomplete':'off'}),
        }
        error_messages = {
            'full_name':{'required':'Full name has required...!'},
            'email':{'required':'Email has required...!'},
            'mobile':{'required':'Mobile number has required...!'},
            'password':{'required':'Password has required...!'},
        }

class UserLogin(forms.Form):
    email = forms.CharField(max_length=30,min_length=10,label='Enter Email ',widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'example@......... ','autocomplete':'off'}),error_messages={
            'required':'Email or Nubers has required...!',
            'min_length':'Usename is too short'})
    password = forms.CharField(max_length=20,label='Password',widget=forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Enter password','autocomplete':'off'}),error_messages={
            'required':'Password has required',
            'min_length':'password is too short'})
