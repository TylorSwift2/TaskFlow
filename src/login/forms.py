"""
Created forms.py to handle the form from login view
"""

from django import forms


class LoginForm(forms.Form):
    """ The class is to handle the form attributes """
    
    user = forms.CharField(max_length=255, required=True,widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'User',
            'id': 'user'
        })) 
    
    password = forms.CharField(
    
        max_length=255, required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'password'
        })
    )
    