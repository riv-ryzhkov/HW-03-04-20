# Generated by Django 2.2.11 on 2020-04-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0002_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='rrr@gmail.com', max_length=128),
        ),
    ]