from django.db import models

# Create your models here.


class Product(models.Model):
    SKU = models.CharField(max_length=4, unique=True)
    Name = models.CharField(max_length=255)
    Qty = models.IntegerField()
    Price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.Name
