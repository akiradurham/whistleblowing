# Generated by Django 5.0.2 on 2024-03-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='text',
            field=models.CharField(default='N/A', max_length=500),
        ),
    ]
