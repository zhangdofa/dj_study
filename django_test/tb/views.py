from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader,RequestContext
# Create your views here.
from tb.models import PhoneInfo

from tb.models import Sales


def index(request):
    # template = loader.get_template('stock/index.html')
    heros = PhoneInfo.objects.all().order_by('-favcount')[:10]
    # print(heros)
    for i in heros:
        print(i.title+'\t'+str(i.favcount))
    jsondata = {
        "key": [i.title for i in heros],
        "value": [i.favcount for i in heros]
    }

    return JsonResponse(jsondata)

def sales(request):
    # template = loader.get_template('stock/index.html')
    heros = Sales.objects.all().order_by('-sales')[:10]
    # print(heros)
    for i in heros:
        print(i.brands + '\t' + str(i.sales))
    jsondata = {
        "key": [i.brands for i in heros],
        "value": [i.sales for i in heros]
    }

    return JsonResponse(jsondata)
    # print(heros)
    # context = RequestContext(request,{'title':'英雄','heros':heros})
    # return HttpResponse(template.render(context))