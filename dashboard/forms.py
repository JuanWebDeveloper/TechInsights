from django import forms
from django.core.exceptions import ValidationError


class ManagePost(forms.Form):
    CATEGORY_CHOICES = [
        ('tech', 'Tecnología'),
        ('life', 'Estilo de Vida'),
        ('edu', 'Educación'),
    ]

    title = forms.CharField(
        label="Título",
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Título del artículo'
        })
    )
    content = forms.CharField(
        label="Contenido",
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe tu artículo aquí...'
        })
    )
    category = forms.ChoiceField(
        label="Categoría",
        choices=[('', 'Seleccionar Categoría')] + CATEGORY_CHOICES,
        required=False,
    )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError("El título no puede estar vacío.")
        if len(title) < 5:
            raise ValidationError(
                "El título debe tener al menos 5 caracteres.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError("El contenido no puede estar vacío.")
        if len(content) < 20:
            raise ValidationError(
                "El contenido debe tener al menos 20 caracteres.")
        return content
