# Generated by Django 3.1.3 on 2020-11-06 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201105_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='spotify_id',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
