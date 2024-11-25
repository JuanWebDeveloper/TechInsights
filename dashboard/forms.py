from django import forms
from django.core.exceptions import ValidationError
from blog.models import Category, Post


class ManagePost(forms.ModelForm):
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
    category = forms.ModelChoiceField(
        queryset=Category.objects.exclude(name='Sin Categoría'),
        label="",
        empty_label="Seleccionar Categoría",
        required=False,
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError("El título no puede estar vacío.")
        if len(title) < 20:
            raise ValidationError(
                "El título debe tener al menos 20 caracteres.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError("El contenido no puede estar vacío.")
        if len(content) < 300:
            raise ValidationError(
                "El contenido debe tener al menos 300 caracteres.")
        return content
