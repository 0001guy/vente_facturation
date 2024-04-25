from django.db import models

class category(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)
    
    def __str__(self):
           return   self.nom

class produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)
    unite = models.CharField(max_length=31)
    quantite = models.FloatField()
    prix_vente = models.FloatField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
      
    def __str__(self):
            return f"{sefl.nom} igurishwa {self.prix_vente}"

class Groupe(models.Model):
    id = models.AutoField(primary_key=True)
    designation_groupe = models.CharField(max_length=20)

    def __str__(self):
        return self.designation_groupe


class Personnel(models.Model):
    id = models.AutoField(primary_key=True)
    noms_user = models.CharField(max_length=20)
    ref_groupe_user = models.ForeignKey(Groupe, on_delete=models.PROTECT)

    def __str__(self):
        return self.noms_user


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    noms_client = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)

    def __str__(self):
        return self.noms_client


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    numero_commande = models.CharField(max_length=20)
    montant_commande = models.DecimalField(max_digits=10, decimal_places=2)
    ref_client_commande = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_commande


class Mesure(models.Model):
    id = models.AutoField(primary_key=True)
    designation_mesure = models.CharField(max_length=100)

    def __str__(self):
        return self.designation_mesure


class Paiement(models.Model):
    id = models.AutoField(primary_key=True)
    numero_recu_paiement = models.CharField(max_length=20)
    montant_paiement = models.DecimalField(max_digits=10, decimal_places=2)
    ref_commande_paiement = models.ForeignKey(Commande, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_recu_paiement


class MesureProduit(models.Model):
    id = models.AutoField(primary_key=True)
    ref_mesure_mesure_produit = models.ForeignKey(Mesure, on_delete=models.CASCADE)
    ref_produit_mesure_produit = models.ForeignKey(produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"MesureProduit {self.id}"


class ProduitCommande(models.Model):
    id = models.AutoField(primary_key=True)
    ref_produit_produit_commande = models.ForeignKey(produit, on_delete=models.CASCADE)
    ref_commande_produit_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)

    def __str__(self):
        return f"ProduitCommande {self.id}"
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    produit = models.ForeignKey(produit, on_delete=models.CASCADE)
    quantite_initiale = models.FloatField(editable=False, null=True)
    quantite_actuelle = models.FloatField(editable=False, null=True)
    created_at = models.DateTimeField(editable=True)
    delai_expiration = models.PositiveIntegerField()
    prix = models.FloatField()
