# Generated by Django 5.0.4 on 2024-05-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_modelform_mother_name_alter_modelform_father_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelform',
            name='boolean_field',
            field=models.BooleanField(default='True'),
        ),
    ]