# Generated by Django 4.2.1 on 2023-12-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='projectrequest',
            options={'verbose_name': 'Запрос на проект', 'verbose_name_plural': 'Запросы на проект'},
        ),
        migrations.AddField(
            model_name='project',
            name='payment',
            field=models.IntegerField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='urgency',
            field=models.DateTimeField(max_length=1000, null=True),
        ),
    ]
