# Generated by Django 2.0.4 on 2018-04-14 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='app_data',
            new_name='app_date',
        ),
    ]