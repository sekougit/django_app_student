from django.db import models

class Eleve(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    note_francais = models.FloatField()
    note_anglais = models.FloatField()
    note_math = models.FloatField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"
