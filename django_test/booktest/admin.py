from django.contrib import admin
from .models import BookInfo, ShortageInfo
from .models import HeroInfo
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date','read','comment','is_delete']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','comment','book','is_delete']
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(ShortageInfo)