# Generated by Django 3.1.7 on 2021-04-17 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20210417_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='patient',
            new_name='user',
        ),
    ]
