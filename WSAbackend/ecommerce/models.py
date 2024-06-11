from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name

class Region(models.Model):
    region_name = models.CharField(max_length=250)

    def __str__(self):
        return self.region_name

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=255)
    stock_quantity = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Cart {self.id} with {self.quantity} of {self.product.product_name}"

class Stock(models.Model):
    product = models.ForeignKey(Product, related_name="stock_product", on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return f"Stock {self.id} for {self.product.product_name} with {self.quantity_in_stock} items"
