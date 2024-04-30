# Generated by Django 5.0.3 on 2024-04-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devise',
            name='devise',
            field=models.CharField(choices=[('EUR', 'EUR (EUR)'), ('GBP', 'GBP (GBP)'), ('USD', 'USD (USD)'), ('CAD', 'CAD (CAD)'), ('AUD', 'AUD (AUD)'), ('JPY', 'JPY (JPY)')], default='EUR', max_length=10),
        ),
    ]