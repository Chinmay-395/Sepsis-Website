# Generated by Django 3.0.8 on 2020-07-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_auto_20200715_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
