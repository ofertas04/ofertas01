# Generated by Django 2.0.8 on 2018-08-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0004_auto_20180815_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='img',
            field=models.FileField(null=True, upload_to='site_1/media/%Y/%m'),
        ),
    ]
