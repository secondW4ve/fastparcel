# Generated by Django 3.1.3 on 2021-11-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20211126_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='paypal_email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]