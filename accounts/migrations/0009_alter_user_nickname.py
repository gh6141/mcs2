# Generated by Django 3.2 on 2022-07-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=150, verbose_name='ニックネーム'),
        ),
    ]