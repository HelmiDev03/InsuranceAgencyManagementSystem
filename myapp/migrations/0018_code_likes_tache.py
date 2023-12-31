# Generated by Django 4.2.3 on 2023-07-18 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('travail', models.FileField(null=True, upload_to='travaux_stagiaires/')),
                ('note', models.IntegerField(default=0)),
                ('stagiaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stagiaire')),
            ],
        ),
    ]
