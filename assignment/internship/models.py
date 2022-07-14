from django.db import models

# # Create your models here.
class category(models.Model):
    categoryname=models.CharField(max_length=50)

class product(models.Model):
    categoryname=models.ForeignKey(category,on_delete=models.DO_NOTHING)
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()
    Quantity=models.IntegerField()
    description=models.CharField(max_length=150)