from django.db import models

# Create your models here.
class BookInfo(models.Model):
    class Meta:
        db_table = 'booktest_bookinfo'
    title = models.CharField(max_length=20)
    pub_date = models.DateField()
    read = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

class HeroInfo(models.Model):
    class Meta:
        db_table = 'booktest_heroinfo'
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    comment = models.CharField(max_length=100)
    book = models.ForeignKey('BookInfo')
    is_delete = models.BooleanField(default=False)

class ShortageInfo(models.Model):
    class Meta:
        db_table = 'shortage'
    storeid = models.CharField(max_length=20)
    storename = models.CharField(max_length=100)
    shortquantity = models.IntegerField(default=0)
    rundate = models.DecimalField(max_digits=20,decimal_places=20)