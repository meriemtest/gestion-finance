# Generated by Django 5.0.3 on 2024-03-29 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('devises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='devise',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='devises.devise'),
        ),
    ]
