# Generated by Django 5.1.1 on 2024-09-11 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='conmirf_password',
            new_name='confirm_password',
        ),
    ]
