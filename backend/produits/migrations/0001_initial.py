# Generated by Django 5.0.3 on 2024-04-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
