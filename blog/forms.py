from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


class SignInForm(forms.Form):
    email = forms.CharField(
        label="Correo Electrónico",
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'juan@ejemplo.com'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput()
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(
                "Por favor, introduce un correo electrónico válido.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 10:
            raise ValidationError(
                "La contraseña debe tener al menos 10 caracteres.")
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "La contraseña debe contener al menos una letra mayúscula.")
        return password


class SignUpForm(forms.Form):
    username = forms.CharField(
        label="Nombre de Usuario",
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Juan Vargas'
        })
    )
    email = forms.CharField(
        label="Correo Electrónico",
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'juan@ejemplo.com'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label="Confirmar Contraseña",
        required=True,
        widget=forms.PasswordInput()
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError(
                "El nombre de usuario debe tener al menos 5 caracteres.")
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError(
                "El nombre de usuario solo puede contener letras, números y guiones bajos.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(
                "Por favor, introduce un correo electrónico válido.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 10:
            raise ValidationError(
                "La contraseña debe tener al menos 10 caracteres.")
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "La contraseña debe contener al menos una letra mayúscula.")
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden.")
        return confirm_password
