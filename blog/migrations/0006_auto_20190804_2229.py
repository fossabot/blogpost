# Generated by Django 2.2.1 on 2019-08-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190804_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bg_pic',
            field=models.ImageField(upload_to='blog/bg_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to='blog/profile_pics'),
        ),
    ]
