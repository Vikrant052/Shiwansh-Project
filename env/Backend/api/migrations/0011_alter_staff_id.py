# Generated by Django 5.1.1 on 2024-10-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
