# Generated by Django 3.2 on 2021-04-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tigID', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0)),
                ('sale', models.BooleanField(default=False)),
                ('sale_price', models.FloatField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('quantity_saled', models.IntegerField(default=0)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]