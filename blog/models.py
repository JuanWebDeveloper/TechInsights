from django.db import models
from django.core.validators import MinLengthValidator


class Category(models.Model):
    name = models.CharField(max_length=50, validators=[
                            MinLengthValidator(5)])
    description = models.TextField(max_length=250, validators=[
                                   MinLengthValidator(50)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
