# Generated by Django 5.0.2 on 2024-04-18 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_anonymoussubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='submissions/')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.submission')),
            ],
        ),
    ]
