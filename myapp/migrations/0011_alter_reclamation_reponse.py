# Generated by Django 4.2.3 on 2023-07-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_reclamation_user_reclamation_employe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamation',
            name='reponse',
            field=models.TextField(max_length=100),
        ),
    ]
