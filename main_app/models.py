from django.db import models


# Create your models here.

class featured(models.Model):
    title = models.CharField(max_length=255)
    cloth_material_category = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    url= models.CharField(max_length=400)
    tags= models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title
    
class carousel(models.Model):
    title = models.CharField(max_length=255)
    cloth_material_category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    url= models.CharField(max_length=400)
    tags= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class occational(models.Model):
    title = models.CharField(max_length=255)
    cloth_material_category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    url= models.CharField(max_length=400)
    tags= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
class formal(models.Model):
    title = models.CharField(max_length=255)
    cloth_material_category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    url= models.CharField(max_length=400)
    tags= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
class casual(models.Model):
    title = models.CharField(max_length=255)
    cloth_material_category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    url= models.CharField(max_length=400)
    tags= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
class kids(models.Model):
    title = models.CharField(max_length=255)
    cloth_material_category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    url= models.CharField(max_length=400)
    tags= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title




