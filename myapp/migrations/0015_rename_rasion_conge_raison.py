# Generated by Django 4.2.3 on 2023-07-17 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_conge_reponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conge',
            old_name='rasion',
            new_name='raison',
        ),
    ]
