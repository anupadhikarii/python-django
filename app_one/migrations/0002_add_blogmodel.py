# Generated by Django 4.0.1 on 2022-02-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=80)),
                ('desc', models.TextField(max_length=8000)),
                ('image', models.ImageField(upload_to='my image')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]