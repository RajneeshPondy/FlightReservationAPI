# Generated by Django 3.1.4 on 2020-12-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0003_auto_20201230_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=10),
        ),
    ]
