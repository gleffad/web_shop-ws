# Generated by Django 3.2 on 2021-04-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigAPI', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
