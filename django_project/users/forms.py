# here we extend the default django form or make a new one

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# this extends the django default usercreation form by adding an email field
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # new extended field

    class Meta:
        model = User  # means save in User table
        fields = ['username', 'email', 'password1', 'password2']    # specifies the order in which the form elemets should be shown


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() 

    class Meta:
        model = User  
        fields = ['username', 'email']   # fieds which are to be updated 


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile  
        fields = ['image']    
