# Generated by Django 5.1.1 on 2024-09-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
