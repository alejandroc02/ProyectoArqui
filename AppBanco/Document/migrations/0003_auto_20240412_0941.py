# Generated by Django 2.1.5 on 2024-04-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0002_auto_20240411_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
