# Generated by Django 3.2.6 on 2024-04-12 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0004_auto_20240412_1700'),
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuario.clientprofile'),
        ),
        migrations.AddField(
            model_name='client',
            name='documents',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Document.document'),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='cell_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Usario',
        ),
    ]
