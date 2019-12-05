from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo,HeroInfo,ShortageInfo
# Create your views here.


def index(request):
    #获取模块
    template = loader.get_template('booktest/index.html')
    #定义上下文
    books = ShortageInfo.objects.all()
    # print(books)
    # for book in books:
    #     print(book.storeid)
    data = {
        'key':[i.rundate for i in books],
        'value':[i.shortquantity for i in books]
    }
    return JsonResponse(data)
def hero(request):
    template = loader.get_template('booktest/hero.html')
    book_id = request.GET.get('book_id')
    heros = HeroInfo.objects.filter(book_id = book_id)
    context = RequestContext(request,{'title':'英雄','heros':heros})
    return HttpResponse(template.render(context))

# def index(request):
#     #获取模块
#     template = loader.get_template('booktest/index.html')
#     #定义上下文
#     books = BookInfo.objects.all()
#     context = RequestContext(request,{'title':'图书','books':books})
#     return HttpResponse(template.render(context))