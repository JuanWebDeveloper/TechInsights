from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


class SignInForm(forms.Form):
    email = forms.CharField(
        label="Correo Electrónico",
        required=True,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input'})
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

        if not re.search(r'[a-z]', password) and not re.search(r'[A-Z]', password):
            raise ValidationError(
                "La contraseña debe contener al menos una letra minúscula y una mayúscula.")

        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "La contraseña debe contener al menos una letra minúscula.")

        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "La contraseña debe contener al menos una letra mayúscula.")
        return password
