# Generated by Django 3.2 on 2021-04-20 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tigAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('date',)},
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='created',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
    ]
