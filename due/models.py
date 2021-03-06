from django.db import models
from category.models import Category


class Due(models.Model):
    due_description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__ (self):
        return self.due_description


class Due_Definition(models.Model):
    time_initial = models.DateField(null=True, blank=True)
    time_end = models.DateField(null=True, blank=True)
    day_pay = models.PositiveSmallIntegerField(default=0)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    due = models.ForeignKey(Due, on_delete=models.CASCADE)
    
