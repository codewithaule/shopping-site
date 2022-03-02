
from django.db import models

from product.models import Product
from .paystack import PayStack

class Order(models.Model):
    amount = models.PositiveIntegerField()
    email = models.EmailField()
    verified =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
  
    class Meta:
        ordering = [ '-created_at',]

    def __str__(self):
        return f"Payment: {self.amount}"
   
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return  '%s' % self.id
        
