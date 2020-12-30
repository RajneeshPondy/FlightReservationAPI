# Generated by Django 3.1.4 on 2020-12-30 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='middle_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightApp.passenger'),
        ),
    ]
