# Generated by Django 3.1.1 on 2022-04-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='patronymic',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=20),
        ),
    ]
