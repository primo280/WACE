from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()
router.register(r'organisations', OrganisationViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'fournisseurs', FournisseurViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'commandes', CommandeViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'historique-prix', HistoriquePrixViewSet)
router.register(r'historique-stock', HistoriqueStockViewSet)
router.register(r'maintenances', MaintenanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
