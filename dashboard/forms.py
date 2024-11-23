from django import forms


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
        required=True,
    )
