from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from area.models import AreaInfo
# Create your views here.
def index(request):
    #获取模块
    template = loader.get_template('area/index.html')
    area = AreaInfo.objects.all()
    context = RequestContext(request,{'title':'hh','data':area})
    return HttpResponse(template.render(context))