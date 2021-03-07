from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    p_name = models.CharField(max_length=100)
    p_image = models.ImageField()
    p_price = models.IntegerField()
    p_desc = models.TextField()
    p_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name
    
    
    