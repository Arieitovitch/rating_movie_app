# Generated by Django 2.2.1 on 2020-04-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0008_auto_20200411_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
