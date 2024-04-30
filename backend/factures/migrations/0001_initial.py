# Generated by Django 5.0.3 on 2024-04-30 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0011_client_devise'),
        ('commandes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactureService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facture_id', models.CharField(editable=False, max_length=20, unique=True)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_comptabilisation', models.DateField(blank=True, null=True)),
                ('date_decheance', models.DateField(blank=True, null=True)),
                ('non_payée', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facture_services', to='clients.client')),
                ('commande_ligne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facture_services', to='commandes.commande_ligne')),
            ],
        ),
        migrations.CreateModel(
            name='FactureVente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facture_id', models.CharField(editable=False, max_length=20, unique=True)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_comptabilisation', models.DateField(blank=True, null=True)),
                ('date_decheance', models.DateField(blank=True, null=True)),
                ('non_payée', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facture_ventes', to='clients.client')),
                ('commande_ligne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facture_ventes', to='commandes.commande_ligne')),
            ],
        ),
    ]
