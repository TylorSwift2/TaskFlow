from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    user = forms.CharField(
        label="Usuário",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome de usuário',
            'class': 'form-control'
        }),
        error_messages={
            'required': _('Por favor, informe seu nome de usuário.')
        }
    )
    
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'class': 'form-control'
        }),
        error_messages={
            'required': _('Por favor, informe sua senha.')
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        password = cleaned_data.get('password')
        
        if not user or not password:
            raise ValidationError(_('Por favor, preencha todos os campos.'))
        
        return cleaned_data


class RegistrationForm(forms.Form):
    user = forms.CharField(
        label="Usuário",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome de usuário',
            'class': 'form-control'
        }),
        error_messages={
            'required': _('Por favor, informe seu nome de usuário.'),
            'max_length': _('O nome de usuário deve ter no máximo 150 caracteres.')
        }
    )
    
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu e-mail',
            'class': 'form-control'
        }),
        validators=[EmailValidator()],
        error_messages={
            'required': _('Por favor, informe seu e-mail.'),
            'invalid': _('Por favor, informe um e-mail válido.')
        }
    )
    
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'class': 'form-control'
        }),
        validators=[validate_password],
        error_messages={
            'required': _('Por favor, informe sua senha.')
        }
    )
    
    password2 = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme sua senha',
            'class': 'form-control'
        }),
        error_messages={
            'required': _('Por favor, confirme sua senha.')
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError(_('As senhas não coincidem.'))
        
        return cleaned_data

    def clean_user(self):
        user = self.cleaned_data.get('user')
        # Você pode adicionar validações específicas para o nome de usuário aqui
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # A verificação se o e-mail já existe será feita no RegistrationService
        return email