from django.db import models


class Bank(models.Model):
    description = models.CharField(max_length=255)

    def __str__ (self):
        return self.description


class Saved_Money(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)


class Receive(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=255)
    time_initial = models.DateField(null=True, blank=True)
    time_end = models.DateField(null=True, blank=True)