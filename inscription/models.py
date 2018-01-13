from django.db import models
from django.utils import timezone

# Create your models here.
"""
class Parent(models.Model):
    prenom_parent = models.CharField(max_length=200)
    nom_parent = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.prenom_parent, self.nom_parent)


class Enfant(models.Model):
    parent = models.ForeignKey(Parent, related_name="enfants", on_delete=models.CASCADE)
    prenom_enfant = models.CharField(max_length=200)
    nom_enfant = models.CharField(max_length=200)
    ecole = models.CharField(max_length=200)
    position_football = models.CharField(max_length=200)
    date_inscription = models.DateTimeField(default=timezone.now)
    age = models.PositiveSmallIntegerField()
    adresse_email = models.EmailField
    a_deja_paye = models.BooleanField(default=False)

    def payer_inscription(self):
        self.a_deja_paye = True
        self.save()

    def __str__(self):
        return "{} {}".format(self.prenom_enfant, self.nom_enfant)
"""
