from django.http import JsonResponse, HttpResponse
from django.template import loader,RequestContext

from django.shortcuts import render

# Create your views here.
from stock.models import Stock,ShortageInfo,Brand_stock


#返回分店库存数据
def index(request):
    storeid = request.GET.get('storeid')
    # print('店铺id:%s'%storeid)
    heros = Stock.objects.filter(storeid = storeid).order_by('-quantity')[:15]
    jsondata = {
            # "k": [i['goodsname'] for i in name],
            "key": [i.goodsname for i in heros],
            "value": [j.quantity for j in heros]
        }

    return JsonResponse(jsondata)
    # context = RequestContext(request,{'title':'英雄','heros':heros})
    # return HttpResponse(template.render(context))
    # print(storeid)

#首页select选择器数据
def home(request):
    template = loader.get_template('stock/index.html')
    storeid = Stock.objects.values('storeid').distinct()
    name = []
    for i in storeid:
        # print(i['storeid'])
        storenames = Stock.objects.filter(storeid=i['storeid'])
        storenames = [j.storename for j in storenames]
        # print(storenames[0])
        storenames = {'storename': storenames[0]}
        name.append(storenames)
    print(name)
    print(storeid)
    store = zip(storeid, name)
    # context = RequestContext(request, {'store': store})

    #缺货
    storeid1 = ShortageInfo.objects.values('storeid').distinct()
    name1 = []
    for i in storeid1:
        # print(i['storeid'])
        storenames = ShortageInfo.objects.filter(storeid=i['storeid'])
        storenames = [j.storename for j in storenames]
        # print(storenames[0])
        storenames = {'storename': storenames[0]}
        name1.append(storenames)
    print(name1)
    print(storeid1)
    store1 = zip(storeid1, name1)
    print(id(store1), id(store))
    print(store1)
    context = RequestContext(request, {'store': store,'store1':store1})
    return HttpResponse(template.render(context))

#返回分店缺货数据
def index1(request):
    #获取模块
    #定义上下文
    # storeid = request.GET.get('storeid')
    # print('店铺id:%s' % storeid)
    # books = ShortageInfo.objects.filter(storeid=storeid)
    books = ShortageInfo.objects.all()
    # print(books)
    # for book in books:
    #     print(book.storeid)
    data = {
        # 'storeid':[i.storeid for i in books],
        'key':[i.rundate for i in books],
        'value':[i.shortquantity for i in books]
    }
    # print(data)
    return JsonResponse(data)

#返回品牌库存数据
def index2(request):
    #获取模块
    #定义上下文
    # storeid = request.GET.get('storeid')
    # print('店铺id:%s' % storeid)
    # books = ShortageInfo.objects.filter(storeid=storeid)
    books = Brand_stock.objects.all().order_by('-quantity')[:10]
    # print(books)
    # for book in books:
    #     print(book.storeid)
    data = {
        'key':[i.brandname for i in books],
        'value':[i.quantity for i in books]
    }
    # print(data)
    return JsonResponse(data)