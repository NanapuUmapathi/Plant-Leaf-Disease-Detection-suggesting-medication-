from django.db import models
"""
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
    
  
# declare a new model with a name "GeeksModel"
class Customer(models.Model):
    # fields of the model
    customerid= models.CharField(max_length = 200)
    customername = models.TextField()
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
"""