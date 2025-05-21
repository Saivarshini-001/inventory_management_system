
# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)  # Name of the inventory item
    quantity = models.IntegerField()          # Quantity in stock
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item

    def __str__(self):
        return self.name  # This will display the item name in admin and elsewhere
