# Generated by Django 2.0.8 on 2018-08-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='img',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
