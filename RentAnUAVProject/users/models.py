from django.db import models
import datetime

# Categories of UAVs
class Category(models.Model):
   name = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name
   
   class Meta:
      verbose_name_plural = 'categories'
   
# Customers   
class Customer(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   email = models.EmailField(max_length=100)
   password = models.CharField(max_length=50)

   def __str__(self):
      return f'{self.first_name} {self.last_name}'

# All of our products
class Product(models.Model):
   brand = models.CharField(max_length=50)
   model = models.CharField(max_length=50)
   weight = models.DecimalField(default=0, decimal_places=2, max_digits=6)
   price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
   description = models.CharField(max_length=250, default='', blank=True)
   image = models.ImageField(upload_to='uploads/UAV/')
   is_rent = models.BooleanField(default=False)
   rent_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

   def __str__(self):
      return f'{self.brand} {self.model}'
   
#User orders
class Order(models.Model):
   uav = models.ForeignKey(Product, on_delete=models.CASCADE)
   user = models.ForeignKey(Customer, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   address = models.CharField(max_length=100, default='', blank=True)
   phone = models.CharField(max_length=50, default='', blank=True)
   date = models.DateField(default=datetime.datetime.today)
   status = models.BooleanField(default=False)

   def __str__(self):
      return self.uav