# Generated by Django 2.2.2 on 2019-08-15 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_songs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Songs',
        ),
    ]