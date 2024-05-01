# Generated by Django 5.0.2 on 2024-03-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('site_admin', models.BooleanField(default=False, verbose_name='Admin User')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('file', models.FileField(upload_to='submissions/')),
            ],
        ),
    ]