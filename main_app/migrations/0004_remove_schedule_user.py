# Generated by Django 3.2.5 on 2021-07-29 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_schedule_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='user',
        ),
    ]