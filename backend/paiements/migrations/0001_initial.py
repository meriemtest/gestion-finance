# Generated by Django 5.0.3 on 2024-04-30 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('type_paiement', models.CharField(choices=[('C', 'Complet'), ('P', 'Partiel')], default='P', max_length=1)),
                ('facture_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factures.factureservice')),
                ('facture_vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factures.facturevente')),
            ],
        ),
    ]
