# Generated by Django 3.2.9 on 2022-01-20 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectalo', '0004_auto_20220120_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='seekerFlag',
            new_name='builderFlag',
        ),
    ]
