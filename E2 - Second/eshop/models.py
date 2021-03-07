from django.db import models
import datetime
from django.db.models import Count
from django.contrib.auth.models import User

class Category(models.Model):
    c_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.c_name

    @staticmethod
    def get_all_categoty():
        return Category.objects.all()

    @staticmethod
    def category_count():
        categories = Category.objects.annotate(Count('product'))
        return categories.values_list('c_name', 'product__count')

    @staticmethod
    def cat(id):
        return Category.objects.filter(product__category=id).count()


class Product(models.Model):
    p_name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    timestamp = models.DateTimeField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_product_category_wise(ids):
        return Product.objects.filter(category=ids)

    @staticmethod
    def get_product_in_cartdetail(ids):
        return Product.objects.filter(id__in=ids)


class Placeorder(models.Model):
    firstname = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.IntegerField()
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    qty = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    price = models.IntegerField()
    
    @staticmethod
    def get_order_by_customer(cus):
       return Placeorder.objects.filter(customer = cus).order_by('-date')


class Comment(models.Model):
    comment = models.TextField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    postby = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)    
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='parentcom')
    commentBy = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.comment