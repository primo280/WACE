from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'role']
    search_fields = ['nom', 'email']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['nom', 'telephone', 'organisation']
    search_fields = ['nom', 'organisation__nom']

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ['nom', 'type_fournisseur', 'organisation']
    search_fields = ['nom', 'organisation__nom']
    
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('client', 'produit', 'quantite','date','statut')
    search_fields = ('client','statut','date')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id','nom')
    search_fields = ('id',)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','nom','description','prix','quantite','categorie','fournisseur','seuil_critique')
    search_fields = ('categorie',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id','produit','quantite')
    search_fields = ('produit',)


@admin.register(HistoriquePrix)
class HistoriquePrixAdmin(admin.ModelAdmin):
    list_display = ('id','produit','date_changement','ancien_prix','nouveau_prix')
    search_fields = ('produit',)

@admin.register(HistoriqueStock)
class HistoriqueStockAdmin(admin.ModelAdmin):
    list_display = ('id','produit','date_changement','quantite_avant','quantite_apres','type_changement')
    search_fields = ('produit',)

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id','produit','type_maintenance','description','date_planifiee','date_intervention','statut')
    search_fields = ('type_maintenance',)

