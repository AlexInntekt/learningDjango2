# Generated by Django 2.0.2 on 2018-07-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restauran',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
