# Generated by Django 2.1.7 on 2019-02-13 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_admin', '0003_meal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
    ]