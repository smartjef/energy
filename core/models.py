from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)
    website = models.URLField()
    address =  models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EnergyConsumption(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.name