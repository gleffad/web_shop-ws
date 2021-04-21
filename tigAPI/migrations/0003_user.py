# Generated by Django 3.2 on 2021-04-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigAPI', '0002_auto_20210420_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_creation_date', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('user_name',),
            },
        ),
    ]
