# Generated by Django 2.0.8 on 2018-08-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo_acesso', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
                ('data_publicacao', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
