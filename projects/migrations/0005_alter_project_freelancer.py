# Generated by Django 4.2.1 on 2023-06-16 10:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_remove_project_user_project_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='freelancer',
            field=models.ManyToManyField(related_name='freelancer_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]