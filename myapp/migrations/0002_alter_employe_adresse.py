# Generated by Django 4.2.3 on 2023-07-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='adresse',
            field=models.CharField(default='nom présisée', max_length=200),
        ),
    ]
