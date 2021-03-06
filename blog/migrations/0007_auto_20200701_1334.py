# Generated by Django 2.0.5 on 2020-07-01 11:34

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200629_1718'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('choice', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('active', 'Active')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('active', 'Active')], default='active', max_length=10),
        ),
    ]
