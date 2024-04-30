# Generated by Django 5.0.3 on 2024-04-26 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_remove_client_devise'),
        ('devises', '0002_alter_devise_devise'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='devise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devises.devise'),
        ),
    ]
