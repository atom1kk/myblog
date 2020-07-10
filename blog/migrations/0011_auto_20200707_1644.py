# Generated by Django 2.0.5 on 2020-07-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200707_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='post',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='review',
        ),
        migrations.AddField(
            model_name='comment',
            name='value',
            field=models.CharField(blank=True, choices=[('5', 'Отлично'), ('4', 'Хорошо'), ('3', 'Нормально'), ('2', 'Плохо'), ('1', 'Ужасно')], max_length=20, null=True, verbose_name='Value'),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]