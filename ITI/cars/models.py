from django.db import models
from django.shortcuts import reverse


# Create your models here.

class FactorInformation(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50, null=False)
    markName = models.CharField(max_length=50, null=False)
    model = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True, )
    updatedAt = models.DateTimeField(auto_now=True)
    factoryInfo = models.ForeignKey(FactorInformation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id, self.name, self.markName, self.model, self.factoryInfo}"

    def get_show_url(self):
        return reverse("car.show", args=[self.id])

    def get_edit_url(self):
        return reverse("car.edit", args=[self.id])

    def get_delete_url(self):
        return reverse("car.delete", args=[self.id])

    def modelChek(self):
        if self.model >= 2020:
            return True
        else:
            return False

    modelChek.short_description = 'Car model is 2020 or above'
    modelChek.boolean = True

    @classmethod
    def getAllCars(cls):
        return cls.objects.all()
