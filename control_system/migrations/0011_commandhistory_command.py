# Generated by Django 3.0.8 on 2020-07-03 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_system', '0010_auto_20200703_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandhistory',
            name='command',
            field=models.TextField(blank=True, null=True),
        ),
    ]
