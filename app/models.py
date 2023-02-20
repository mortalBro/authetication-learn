from django.db import models


class Employe(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=40)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

