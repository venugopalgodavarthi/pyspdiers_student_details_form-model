# Generated by Django 3.2.4 on 2022-01-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentform', '0002_alter_form_usn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Location',
            field=models.CharField(max_length=150),
        ),
    ]
