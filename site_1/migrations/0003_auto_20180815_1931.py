# Generated by Django 2.0.8 on 2018-08-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0002_produto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='img',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
