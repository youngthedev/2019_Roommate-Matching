# Generated by Django 2.1.8 on 2019-05-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='like_dorm',
            field=models.TextField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_info1',
            field=models.TextField(blank=True, max_length=20),
        ),
    ]
