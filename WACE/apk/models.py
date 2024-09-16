from django.db import models



class Organisation(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    motdepasse = models.CharField(max_length=255, null=True, blank=True)  # Hashé dans un vrai cas
    role = models.CharField(max_length=50, choices=[('client', 'Client'), ('fournisseur', 'Fournisseur')], null=True, blank=True)

    def __str__(self):
        return self.nom

class Client(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nom

class Fournisseur(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    TYPE_FOURNISSEUR = [
        ('direct', 'Direct'),
        ('indirect', 'Indirect'),
    ]
    type_fournisseur = models.CharField(max_length=10, choices=TYPE_FOURNISSEUR, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} - {self.get_type_fournisseur_display()}"

class Categorie(models.Model):
    nom = models.CharField(max_length=255)


class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.FloatField()
    quantite = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    seuil_critique = models.IntegerField(default=10)  # Nouveau champ pour seuil critique

    def __str__(self):
        return self.nom

    def check_seuil_critique(self):
        if self.quantite <= self.seuil_critique:
            # Logique pour déclencher une commande automatique ou envoyer une alerte
            print(f"Le produit {self.nom} est en dessous du seuil critique!")
            self.commander_stock()

    def commander_stock(self):
        # Logique pour commander automatiquement du stock
        print(f"Commande de réapprovisionnement automatique pour {self.nom}")
        # Crée une commande au fournisseur par exemple
        Commande.objects.create(
            produit=self,
            quantite=50,  # Par exemple, on commande 50 unités
            client=None,  # Aucun client car c'est une commande fournisseur
            statut='en_attente'
        )

class Stock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} en stock"



class Commande(models.Model):
    STATUTS = [
        ('en_attente', 'En attente'),
        ('expediee', 'Expédiée'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUTS, default='en_attente')

    def __str__(self):
        return f"Commande {self.id} - {self.produit.nom}"


class HistoriquePrix(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_changement = models.DateField(auto_now_add=True)
    ancien_prix = models.FloatField()
    nouveau_prix = models.FloatField()

    def __str__(self):
        return f"Changement prix {self.produit.nom} du {self.date_changement}"

class HistoriqueStock(models.Model):
    TYPE_CHANGEMENT = [
        ('ajout', 'Ajout'),
        ('retrait', 'Retrait')
    ]
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_changement = models.DateField(auto_now_add=True)
    quantite_avant = models.IntegerField()
    quantite_apres = models.IntegerField()
    type_changement = models.CharField(max_length=10, choices=TYPE_CHANGEMENT)

    def __str__(self):
        return f"Changement stock {self.produit.nom} du {self.date_changement}"

class Maintenance(models.Model):
    TYPE_MAINTENANCE = [
        ('preventive', 'Préventive'),
        ('curative', 'Curative'),
    ]
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    type_maintenance = models.CharField(max_length=10, choices=TYPE_MAINTENANCE)
    description = models.TextField()
    date_planifiee = models.DateField(null=True, blank=True)
    date_intervention = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=20, default='en_attente')

    def __str__(self):
        return f"{self.type_maintenance} - {self.produit.nom}"

