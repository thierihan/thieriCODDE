# Generated by Django 3.1 on 2020-08-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to='img/profile'),
        ),
    ]
