# Generated by Django 4.2.3 on 2023-08-23 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0020_alter_application_applicationdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Step',
            field=models.CharField(default='start', max_length=255),
        ),
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 12, 5, 3, 461255)),
        ),
    ]