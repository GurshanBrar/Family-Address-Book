# Generated by Django 3.0.5 on 2020-06-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familybook', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='phone_number',
            field=models.CharField(max_length=16, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='zip_code',
            field=models.CharField(max_length=5, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=16, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='blank_profile_pic.png', upload_to='images/', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(max_length=5, verbose_name='Zip Code'),
        ),
    ]
