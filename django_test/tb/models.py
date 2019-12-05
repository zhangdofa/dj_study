from django.db import models

# Create your models here.
class PhoneInfo(models.Model):
    class Meta:
        db_table = 'work'
    title = models.CharField(max_length=255)
    favcount = models.IntegerField()

class Sales(models.Model):
    class Meta:
        db_table = 'sales'
    brands = models.CharField(max_length=255)
    sales = models.IntegerField()