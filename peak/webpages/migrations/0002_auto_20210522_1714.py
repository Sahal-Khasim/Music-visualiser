# Generated by Django 3.2.3 on 2021-05-22 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defaultsongs',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='defaultsongs',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='defaultsongs',
            name='image',
        ),
    ]