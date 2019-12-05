from django.db import models

# Create your models here.
class AreaInfo(models.Model):
    class Meta:
        db_table = 'area_areainfo'
    title = models.CharField(max_length=30)
    parent = models.ForeignKey('self', null=True, blank=True)