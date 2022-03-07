from django.db import models
from jsonfield import JSONField

# Create your models here.
from django.db import models
from core.constants import (sub_categories, product_types, categories, order_status)
# Create your models here.


class Brand(models.Model):
    brand_name = models.CharField(max_length=30)


class Product(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    image_url = models.CharField(max_length=600)
    product_type = models.CharField(max_length=50, choices=product_types)
    name = models.CharField(max_length=200)
    options = JSONField()
    highlights = models.TextField(max_length=800)
    specifications = JSONField()
    offers = models.TextField(max_length=200)
    gender = models.CharField(max_length=2)
    category = models.CharField(max_length=50, choices=categories)
    subcategory = models.CharField(max_length=50, choices=sub_categories)
    brand = models.ForeignKey(Brand, on_delete=models.SET_DEFAULT, default="NA")
    related = JSONField(null=True)

    def __str__(self) -> str:
        return self.sku


class Order(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=order_status, default=order_status[0])

    def __str__(self) -> str:
        return str(self.id)


class OrderCatalogue(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=50)
    option = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return str(self.order_id)


class Address(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    pin = models.IntegerField()
    address_line_1 = models.TextField(max_length=100)
    address_line_2 = models.TextField(max_length=100, null=True)
    phone = models.CharField(max_length=15)
    email_id = models.EmailField(max_length=30)
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=60, null=True)

    def __str__(self) -> str:
        return str(self.order_id)





