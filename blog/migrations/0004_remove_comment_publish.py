# Generated by Django 2.0.5 on 2020-06-29 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200629_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='publish',
        ),
    ]
