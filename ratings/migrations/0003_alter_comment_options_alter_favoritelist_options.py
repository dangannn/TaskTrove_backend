# Generated by Django 4.2.1 on 2023-12-06 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='favoritelist',
            options={'verbose_name': 'Список избранных', 'verbose_name_plural': 'Списки избранных'},
        ),
    ]
