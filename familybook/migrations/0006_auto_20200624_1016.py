# Generated by Django 3.0.5 on 2020-06-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familybook', '0005_auto_20200624_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='images/blank_profile_pic.png', upload_to='images/', verbose_name='Profile Picture'),
        ),
    ]
