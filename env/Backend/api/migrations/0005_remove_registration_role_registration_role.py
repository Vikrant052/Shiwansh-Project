# Generated by Django 5.1.1 on 2024-09-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_registration_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='Role',
        ),
        migrations.AddField(
            model_name='registration',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Staff', 'Staff'), ('Student', 'Student')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]