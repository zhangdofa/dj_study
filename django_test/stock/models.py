from django.db import models

# Create your models here.
class Stock(models.Model):
    class Meta:
        db_table = 'stocks'
    storeid = models.CharField(max_length=20)
    storename = models.CharField(max_length=100)
    goodsid = models.CharField(max_length=20)
    goodsname = models.CharField(max_length=100)
    quantity = models.IntegerField()
# class Quehuo(models.Model):
#     class Meta:
#         db_table = 'out_of_stock'
#     rundate = models.DateTimeField()
#     storeid = models.CharField(max_length=255)
#     ooscount = models.IntegerField()
# class Brand(models.Model):
#     class Meta:
#         db_table = 'brand'
#     brandid = models.CharField(max_length=255)
#     brandname = models.CharField(max_length=255)
# class Goods(models.Model):
#     class Meta:
#         db_table = 'goods'
#     goodsid = models.IntegerField()
#     goodsname = models.CharField(max_length=255)
#     brand = models.CharField(max_length=255)
# class Stores(models.Model):
#     class Meta:
#         db_table = 'stores'
#     storeid = models.CharField(max_length=255)
#     storename = models.CharField(max_length=255)
class ShortageInfo(models.Model):
    class Meta:
        db_table = 'shortage'
    storeid = models.CharField(max_length=20)
    storename = models.CharField(max_length=100)
    shortquantity = models.IntegerField(default=0)
    rundate = models.DecimalField(max_digits=20,decimal_places=20)

class Brand_stock(models.Model):
    class Meta:
        db_table = 'brand_stock'
    brandid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10,decimal_places=0)