# Generated by Django 3.2.4 on 2021-08-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_auto_20210819_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('r', 'romantik'), ('d', 'dromatik'), ('h', 'horror'), ('m', 'melodram')], max_length=10),
        ),
    ]
