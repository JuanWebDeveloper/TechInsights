from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
        if not User.objects.filter(email=email).exists():
            raise ValidationError(
                "El correo electrónico no está registrado. Por favor, regístrate.")
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

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            getUser = User.objects.get(email=email)
            user = authenticate(username=getUser.username, password=password)

            if user is None:
                raise ValidationError(
                    "Correo electrónico o contraseña incorrectos.")
        return cleaned_data


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
        if len(username) > 15:
            raise ValidationError(
                "El nombre de usuario debe tener un máximo de 15 caracteres.")
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError(
                "El nombre de usuario solo puede contener letras, números y guiones bajos.")
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                "Este nombre de usuario ya se encuentra registrado.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(
                "Por favor, introduce un correo electrónico válido.")

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Este correo electrónico ya se encuentra registrado.")
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
