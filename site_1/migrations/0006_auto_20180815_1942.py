# Generated by Django 2.0.8 on 2018-08-15 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0005_auto_20180815_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='img',
            field=models.FileField(null=True, upload_to='media/%Y/%m/%d'),
        ),
    ]
