# Generated by Django 5.0.4 on 2024-04-24 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('noms_client', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('designation_groupe', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mesure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('designation_mesure', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_commande', models.CharField(max_length=20)),
                ('montant_commande', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ref_client_commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vente.client')),
            ],
        ),
        migrations.CreateModel(
            name='MesureProduit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ref_mesure_mesure_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vente.mesure')),
                ('ref_produit_mesure_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vente.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_recu_paiement', models.CharField(max_length=20)),
                ('montant_paiement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ref_commande_paiement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vente.commande')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('noms_user', models.CharField(max_length=20)),
                ('ref_groupe_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vente.groupe')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitCommande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ref_commande_produit_commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vente.commande')),
                ('ref_produit_produit_commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vente.produit')),
            ],
        ),
    ]
