# Generated by Django 2.0.4 on 2018-04-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20180414_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='app_date',
            field=models.DateTimeField(null=True, verbose_name='Appointment date'),
        ),
    ]