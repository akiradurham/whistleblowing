# Generated by Django 5.0.2 on 2024-04-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_delete_anonymousfile_delete_anonymoussubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='tag',
            field=models.CharField(choices=[('Cheating - Exam', 'Cheating - Exam'), ('Cheating - Coursework', 'Cheating - Coursework'), ('Lying', 'Lying'), ('Stealing - Physical Property', 'Stealing - Physical Property'), ('Stealing - Coursework', 'Stealing - Physical Property'), ('Plagiarism', 'Plagiarism'), ('Multiple Submission', 'Multiple Submission'), ('False Citation', 'False Citation'), ('False Data', 'False Data'), ('Discrimination', 'Discrimination'), ('Other', 'Other')], default='Other', max_length=40),
        ),
    ]
