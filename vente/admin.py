from django.contrib import admin
from .models import category,produit,Groupe,Personnel,Client,Commande,Mesure,Paiement,MesureProduit,ProduitCommande,stock

admin.site.register(category)
admin.site.register(produit)
admin.site.register(Groupe)
admin.site.register(Personnel)
admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Mesure)
admin.site.register(Paiement)
admin.site.register(MesureProduit)
admin.site.register(ProduitCommande)
admin.site.register(stock)

# Register your models here.
