# Generated by Django 4.1.4 on 2022-12-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_data_predictions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='predictions',
        ),
        migrations.AddField(
            model_name='data',
            name='prediction',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
