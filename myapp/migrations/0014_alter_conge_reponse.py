# Generated by Django 4.2.3 on 2023-07-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_conge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conge',
            name='reponse',
            field=models.TextField(default='non', max_length=100),
        ),
    ]
