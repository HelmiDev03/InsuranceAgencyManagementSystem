# Generated by Django 4.2.3 on 2023-07-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_stagiaire_employe_alter_stagiaire_encadrant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='adresse',
            field=models.CharField(default='not mentioned', max_length=200),
        ),
    ]
