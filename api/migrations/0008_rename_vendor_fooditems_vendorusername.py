# Generated by Django 3.2.4 on 2022-10-31 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20221031_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditems',
            old_name='vendor',
            new_name='vendorusername',
        ),
    ]