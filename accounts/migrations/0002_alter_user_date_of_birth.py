# Generated by Django 3.2 on 2022-06-26 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today, verbose_name='dateofbirth'),
        ),
    ]
