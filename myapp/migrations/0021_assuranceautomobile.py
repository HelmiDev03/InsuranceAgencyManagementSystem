# Generated by Django 4.2.3 on 2023-07-20 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_rename_tache_tache_etat'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssuranceAutomobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('date_premiercirculation', models.DateField()),
                ('usage', models.CharField(max_length=100)),
                ('couverture', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
            ],
        ),
    ]
