# Generated by Django 2.1.5 on 2024-04-12 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CreditCard', '0001_initial'),
        ('Document', '0003_auto_20240412_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('cell_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('profession', models.CharField(max_length=255)),
                ('ciiu_economic_activity', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('income', models.CharField(max_length=255)),
                ('expense', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('creditCard', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='CreditCard.creditCard')),
                ('document', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Document.Document')),
            ],
        ),
    ]
