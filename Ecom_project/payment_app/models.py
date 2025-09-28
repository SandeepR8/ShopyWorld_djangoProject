from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='shipping')
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_phone = models.CharField(max_length=15,null=True,blank=True)
    shipping_state = models.CharField(max_length=100,null=True,blank=True)
    shipping_Address1 = models.CharField(max_length=400)
    shipping_Address2 = models.CharField(max_length=400,null=True,blank=True)
    shipping_city = models.CharField(max_length=70)
    shipping_zipcode = models.CharField(max_length=255,null=True,blank=True)
    shipping_country = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):
        return f"Shipping Address is of {self.shipping_full_name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='store_orders')
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Shipping_Address = models.TextField()
    amount_pay = models.DecimalField(max_digits=5,max_length=20,decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'ordered - {self.id}'

    

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='store_orderItem')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=7,decimal_places=2,max_length=20)

    def __str__(self):
        return f'order item - {self.id}'

