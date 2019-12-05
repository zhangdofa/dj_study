from django.contrib import admin

# Register your models here.
from .models import Stock,ShortageInfo, Brand_stock

admin.site.register(Stock)
# admin.site.register(Quehuo)
# admin.site.register(Goods)
# admin.site.register(Brand)
# admin.site.register(Stores)
admin.site.register(ShortageInfo)
admin.site.register(Brand_stock)