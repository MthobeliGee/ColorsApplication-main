# Generated by Django 4.2.3 on 2023-07-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_alter_represantative_represantativeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='represantative',
            name='RepresantativeId',
            field=models.AutoField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
