from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    email = models.EmailField()
    product_availed = models.CharField(max_length=50)
    service_provider = models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
