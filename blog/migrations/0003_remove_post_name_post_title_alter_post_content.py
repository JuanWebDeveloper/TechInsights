# Generated by Django 5.1.3 on 2024-11-24 07:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_alter_category_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Default Title', max_length=100, validators=[django.core.validators.MinLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(300)]),
        ),
    ]