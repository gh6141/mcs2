# Generated by Django 3.2 on 2022-06-25 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kekkonreki',
            old_name='sake',
            new_name='kekkonreki',
        ),
    ]
