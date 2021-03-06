# Generated by Django 3.1.3 on 2021-11-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211116_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pickup_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
