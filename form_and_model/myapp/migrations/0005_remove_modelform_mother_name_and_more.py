# Generated by Django 5.0.4 on 2024-05-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_modelform_boolean_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelform',
            name='mother_name',
        ),
        migrations.AddField(
            model_name='modelform',
            name='date_time_field',
            field=models.DateTimeField(default='2024-05-24 15:30:00.123456'),
        ),
    ]
