# Generated by Django 5.0.4 on 2024-04-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='male', max_length=10),
        ),
    ]
