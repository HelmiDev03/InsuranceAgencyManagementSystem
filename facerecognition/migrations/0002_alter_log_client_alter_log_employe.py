# Generated by Django 4.2.3 on 2023-08-08 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_code_date'),
        ('facerecognition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.client'),
        ),
        migrations.AlterField(
            model_name='log',
            name='employe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.employe'),
        ),
    ]
