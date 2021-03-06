# Generated by Django 2.0.5 on 2020-06-29 15:03

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200618_1450'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('commented', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/posts_images/'),
        ),
    ]
