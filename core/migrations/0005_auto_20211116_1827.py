# Generated by Django 3.1.3 on 2021-11-16 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='craeted_at',
            new_name='created_at',
        ),
    ]
