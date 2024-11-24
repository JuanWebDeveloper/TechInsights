from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, validators=[
                            MinLengthValidator(5)])
    description = models.TextField(max_length=250, validators=[
                                   MinLengthValidator(50)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post((models.Model)):
    title = models.CharField(max_length=100, validators=[
        MinLengthValidator(20)])
    content = models.TextField(validators=[
        MinLengthValidator(300)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + '- by ' + self.author.username
