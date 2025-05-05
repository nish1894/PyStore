from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    description=models.TextField(blank=True)
    image = models.URLField()
    inventory = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places =2)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    rating_count = models.PositiveIntegerField(default=0)
    title= models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True ,related_name='products')

    def __str__(self):
        return self.title