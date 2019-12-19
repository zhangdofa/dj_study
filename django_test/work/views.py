import os

import time

import re
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader, RequestContext
# from Userstest.models import UsersInfo,HeroInfo,ShortageInfo
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

# from django_test.settings import MEDIA_ROOT

from work.froms import UserForm,Login,Uppassword,Upphone,Radio
from work.models import Users, UserInfo


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def test(request):
    # Users_list = []
    # for i in range(100):
    #
    #     # Users = Users(title = 'Users_%s'%i,price = i*i)
    #     # Users_list.append(Users)
    #     Users = Users(title = 'Users_%s'%i,price = i*i)
    #     Users_list .append(Users)
    #
    # Users.objects.bulk_create(Users_list)  #builk_create 是批量创建数据





    # print(Paginator.count) #总数据量
    # print(Paginator.num_pages) #分页数
    # print(Paginator.page_range) #显示的是页数的标记 就是按钮的数目



    # Users_list = Users.objects.all()
    # paginator = Paginator(Users_list, 2)  #设置每一页显示几条  创建一个panginator对象

    # try:
    #     current_num = int(request.GET.get('page',1))
    #
    #     Users_list = paginator.page(current_num)



    # print(paginator.count)  #通过你创建的对象来调用pangnator的属性  这个是统计总数
    # print(paginator.num_pages)  #因为你上面设置了每一页显示两条  这个分页就会是总数除去每一页的显示的数量
    # print(paginator.page_range)
    # Users_list = paginator.page(1)   #这个是对你的分页的数据进行取值  去除你的分过后的第一页
    # # Users_list ，   paginator.page是取你的分页后的某一页
    # print(Users_list)

    Users_list = Users.objects.all()
    print(Users_list)
    paginator = Paginator(Users_list, 2)  # 设置每一页显示几条  创建一个panginator对象

    try:
        current_num = int(request.GET.get('page',1))  #当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list = paginator.page(current_num)
    except EmptyPage:
            Users_list = paginator.page(4)  #当你输入的page是不存在的时候就会报错

    if paginator.num_pages > 11:  # 如果分页的数目大于11
            if current_num - 5 < 1:  # 你输入的值
                pageRange = range(1, 11)  # 按钮数
            elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
                pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数

            else:
                pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示

    else:
        pageRange = paginator.page_range  # 正常分配





    return render(request,'work/test.html',locals())

def find(request):
    keyword = request.GET.get('keyword')
    print(keyword)
    username = request.session.get("username")
    login_msg = request.session.get('login_msg')
    register_msg = request.session.get('register_msg')
    uppwd_msg = request.session.get('uppwd_msg')
    print(uppwd_msg)
    if login_msg:
        del request.session['login_msg']
    if register_msg:
        del request.session['register_msg']
    if uppwd_msg:
        del request.session['uppwd_msg']
    print(username)
    # video = Users.objects.filter(username=username)
    # url = [j.headimg for j in video]
    if keyword:
        Users_list = Users.objects.filter(headimg__contains=keyword).order_by('-uptime')
        if Users_list:
            print('有记录')
            paginator = Paginator(Users_list, 12)  # 设置每一页显示几条  创建一个panginator对象
            try:
                current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
                Users_list = paginator.page(current_num)
            except EmptyPage:
                Users_list = paginator.page(4)  # 当你输入的page是不存在的时候就会报错
            if paginator.num_pages > 11:  # 如果分页的数目大于11
                if current_num - 5 < 1:  # 你输入的值
                    pageRange = range(1, 11)  # 按钮数
                elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
                    pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
                else:
                    pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
            else:
                pageRange = paginator.page_range  # 正常分配
            # return render(request,'work/test.html',locals())
            if username:
                print('有cookie')
                no_error = None
                find_error = None
                return render_to_response('work/home.html', locals())
            else:
                # username = ''
                print('没有cookie')
                no_error = None
                find_error = None
                return render_to_response('work/home.html', locals())
        else:
            print('哈哈')
            request.session['no_error'] = '抱歉！没有找到你想要的内容！'
            return HttpResponseRedirect('/work/home',{'no_error':'抱歉！没有找到你想要的内容！'})
    else:
        request.session['find_error'] = '您未输入搜索内容！请输入后重试！'
        return HttpResponseRedirect('/work/home',{'find_error':'您未输入搜索内容！请输入后重试！'})

def play(request):
    username = request.session.get("username")
    login_msg1 = request.session.get("login_msg1")
    register_msg1 = request.session.get("register_msg1")
    url = request.GET.get('url')
    if login_msg1:
        del request.session["login_msg1"]
    if register_msg1:
        del request.session["register_msg1"]
    print(url)
    print(username)
    # video = Users.objects.filter(username=username)
    # url = [j.headimg for j in video]
    # Users_list = Users.objects.all()
    if username:
        print('有cookie')
        return render_to_response('work/playpage.html', locals())
    else:
        # username = ''
        print('没有cookie')
        return render_to_response('work/playpage.html', locals())
def play1(request):
    username = request.session.get("username")
    login_msg1 = request.session.get("login_msg1")
    register_msg1 = request.session.get("register_msg1")
    url = request.GET.get('url')
    if login_msg1:
        del request.session["login_msg1"]
    if register_msg1:
        del request.session["register_msg1"]
    print(url)
    print(username)
    # video = Users.objects.filter(username=username)
    # url = [j.headimg for j in video]
    # Users_list = Users.objects.all()
    if username:
        print('有cookie')
        return render_to_response('work/playpage1.html', locals())
    else:
        # username = ''
        print('没有cookie')
        return render_to_response('work/playpage1.html', locals())

@csrf_exempt
def upimg(request):
    username = request.session.get("username")
    print(username)
    if request.method == 'POST':
        print('hhh')
        # username = request.POST['username']  # 获取username
        myfile = request.FILES.get('myfile1', None)  # 获取files二进制流，如果没上传为None
        if myfile is None:
            print('我是谁')
        print(myfile)
        if myfile:
            with open('F:/python project/dj_study/django_test/static/imgs/{0}'.format(username +"_"+ myfile.name), 'wb') as f:
                for data in myfile.chunks():
                    f.write(data)
                # user = UserInfo()  # 存储到数据库，img为存储的文件名，使用时，加上上传文件路径即可
                UserInfo.objects.filter(username=username).update(image=username+"_"+myfile.name)
                # user.username = username
                # user.image = myfile.name
                # user.save()
                request.session['up_msg1'] = '上传成功！'
                return HttpResponseRedirect("/work/person/")
    return HttpResponse('上传失败!请选择图片后再上传')

@csrf_exempt
def upvideo(request):
    username = request.session.get("username")
    # 上传视频
    if request.method == 'POST':
        print('hhh')
        print('hhhhh')
        radio = request.POST.get('radio')  # 获取username
        # radio = Radio(request.POST)
        print(radio)
        # if radio:
        # if radio.is_valid():
        #     print('进来了')
        #     classfi = radio.cleaned_data['radio']
        #     print(classfi)
        #     if classfi:
        # else:
        #     return render_to_response('work/person.html',{'class_error':'您未选择视频分类，请选择后上传！'})
        myfile = request.FILES.get('myfile', None)  # 获取files二进制流，如果没上传为None
        # print(len(myfile.name))
        if myfile is None:
            request.session['none_error'] = '您未选择视频！请选择后上传！'
            print('我是谁')
            return HttpResponseRedirect('/work/person')
        print(myfile)
        if myfile and len(myfile.name) <= 37:
            exsit = Users.objects.filter(username=username,headimg=myfile.name)
            if exsit:
                request.session['exsit_msg'] = '已经上传过该视频！'
                return HttpResponseRedirect('/work/person')
            else:
                if radio:
                    with open('F:/python project/dj_study/django_test/static/media/{0}'.format(myfile.name), 'wb') as f:
                        for data in myfile.chunks():
                            f.write(data)
                        user = Users()  # 存储到数据库，img为存储的文件名，使用时，加上上传文件路径即可
                        user.username = username
                        user.headimg = myfile.name
                        user.classfi = radio
                        user.uptime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                        user.status = 1 #待审核
                        user.save()
                        request.session['up_msg'] = '上传成功！'
                        return HttpResponseRedirect("/work/person/")
                else:
                    print('在这里')
                    request.session['class_error'] = '上传失败'
                    return HttpResponseRedirect('/work/person',{'class_error':'上传失败！'})
        else:
            request.session['length_error'] = '文件名长度请勿超过37！请重命名您的文件！'
            return HttpResponseRedirect('/work/person',{'length_error':'文件名长度请勿超过37！请重命名您的文件！'})
    return HttpResponse('请选择视频后上传！')
def index(request):
    username = request.session.get("username")
    login_msg = request.session.get('login_msg')
    register_msg = request.session.get('register_msg')
    uppwd_msg = request.session.get('uppwd_msg')
    find_error = request.session.get('find_error')
    no_error = request.session.get('no_error')
    print(uppwd_msg)
    print("没有")
    print(no_error)
    if login_msg:
        del request.session['login_msg']
    if register_msg:
        del request.session['register_msg']
    if uppwd_msg:
        del request.session['uppwd_msg']
    if find_error:
        del request.session['find_error']
    if no_error:
        del request.session['no_error']
    print(username)
    # video = Users.objects.filter(username=username)
    # url = [j.headimg for j in video]
    Users_list = Users.objects.filter(classfi='计算机',status=2).order_by('-uptime')
    print(Users_list)
    paginator = Paginator(Users_list, 12)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = int(request.GET.get('page',1))  #当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list = paginator.page(current_num)
    except EmptyPage:
            Users_list = paginator.page(4)  #当你输入的page是不存在的时候就会报错
    if paginator.num_pages > 11:  # 如果分页的数目大于11
            if current_num - 5 < 1:  # 你输入的值
                pageRange = range(1, 11)  # 按钮数
            elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
                pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
            else:
                pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        pageRange = paginator.page_range  # 正常分配
    # return render(request,'work/test.html',locals())
    if username:
        print('有cookie')
        return render_to_response('work/home.html',locals())
    else:
        # username = ''
        print('没有cookie')
        return render_to_response('work/home.html',locals())

def index1(request):
    username = request.session.get("username")
    login_msg = request.session.get('login_msg')
    register_msg = request.session.get('register_msg')
    uppwd_msg = request.session.get('uppwd_msg')
    no_error = None
    find_error = None
    print(uppwd_msg)
    if login_msg:
        del request.session['login_msg']
    if register_msg:
        del request.session['register_msg']
    if uppwd_msg:
        del request.session['uppwd_msg']
    print(username)
    # video = Users.objects.filter(username=username)
    # url = [j.headimg for j in video]
    Users_list = Users.objects.filter(classfi='外语',status=2).order_by('-uptime')
    print(Users_list)
    paginator = Paginator(Users_list, 12)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = int(request.GET.get('page',1))  #当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list = paginator.page(current_num)
    except EmptyPage:
            Users_list = paginator.page(4)  #当你输入的page是不存在的时候就会报错
    if paginator.num_pages > 11:  # 如果分页的数目大于11
            if current_num - 5 < 1:  # 你输入的值
                pageRange = range(1, 11)  # 按钮数
            elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
                pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
            else:
                pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        pageRange = paginator.page_range  # 正常分配
    # return render(request,'work/test.html',locals())
    if username:
        print('有cookie')
        return render_to_response('work/home.html',locals())
    else:
        # username = ''
        print('没有cookie')
        return render_to_response('work/home.html',locals())

def index2(request):
    username = request.session.get("username")
    login_msg = request.session.get('login_msg')
    register_msg = request.session.get('register_msg')
    uppwd_msg = request.session.get('uppwd_msg')
    no_error = None
    find_error = None
    print(uppwd_msg)
    if login_msg:
        del request.session['login_msg']
    if register_msg:
        del request.session['register_msg']
    if uppwd_msg:
        del request.session['uppwd_msg']
    print(username)
    # video = Users.objects.filter(username=username)
    # url = [j.headimg for j in video]
    Users_list = Users.objects.filter(classfi='考研',status=2).order_by('-uptime')
    print(Users_list)
    paginator = Paginator(Users_list, 12)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = int(request.GET.get('page',1))  #当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list = paginator.page(current_num)
    except EmptyPage:
            Users_list = paginator.page(4)  #当你输入的page是不存在的时候就会报错
    if paginator.num_pages > 11:  # 如果分页的数目大于11
            if current_num - 5 < 1:  # 你输入的值
                pageRange = range(1, 11)  # 按钮数
            elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
                pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
            else:
                pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        pageRange = paginator.page_range  # 正常分配
    # return render(request,'work/test.html',locals())
    if username:
        print('有cookie')
        return render_to_response('work/home.html',locals())
    else:
        # username = ''
        print('没有cookie')
        return render_to_response('work/home.html',locals())

def logout(request):
    # request.session.clear() # 删除session
    username = request.session.get('username')
    if username:
        del request.session['username']
    userform = UserForm()
    return HttpResponseRedirect("/work/home", {"username": userform})

def logout1(request):
    url = request.GET.get('url')
    print('已经退出了')
    print(url)
    request.session.clear() # 删除session
    userform = UserForm()
    return HttpResponseRedirect("/work/playpage?url="+ url, {"username": userform})

def logout2(request):
    url = request.GET.get('url')
    print('已经退出了')
    print(url)
    request.session.clear() # 删除session
    userform = UserForm()
    return HttpResponseRedirect('/work/login', {"username": userform})

@csrf_exempt
def home(request):
    template = loader.get_template('work/index.html')
    print('jjjj')
    if request.method == 'POST':
        print('hhh')
        # username = request.POST['username']  # 获取username
        login_msg = request.session.get("login_msg")
        print(login_msg)
        if login_msg:
            del request.session['login_msg']
        myfile = request.FILES.get('myfile', None)  # 获取files二进制流，如果没上传为None
        if myfile is None:
            print('我是谁')
        print(myfile)
        # filename = os.path.join(MEDIA_ROOT, myfile.name).replace('\\',
        #                                                           '/')  # 定义上传的文件名（绝对路径），UPLOADFILE为settings中定义的文件上传路径
        # print(filename)
        # if not os.path.exists('media/'+ myfile.name):
        #     print('文件夹', 'media/'+ myfile.name, '不存在，重新建立')
        #     # os.mkdir(file_path)
        #     os.makedirs('media/'+ myfile.name)
        # filepath = 'media/'+ myfile.name
        # if not os.path.isdir('media'):
        #     os.mkdir(new_path)
        if myfile:
            with open('F:/python project/dj_study/django_test/work/media/{0}'.format(myfile.name), 'wb') as f:
                for data in myfile.chunks():
                    f.write(data)
                    # messages.success(request, "哈哈哈")
                    # context = RequestContext(request, {'messages': messages})
                    # return HttpResponse(template.render(context))
                user = Users()  # 存储到数据库，img为存储的文件名，使用时，加上上传文件路径即可
                user.username = 'zhangsan'
                user.headimg = myfile.name
                user.save()
                return HttpResponseRedirect("/work/person/")

    context = RequestContext(request, {'title': '英雄'})
    return HttpResponse(template.render(context))  # 上传后返回页面

@csrf_exempt
def person(request):
    username = request.session['username']
    msg = request.session.get('msg')
    up_msg = request.session.get('up_msg')
    up_msg1 = request.session.get('up_msg1')
    upphone_msg = request.session.get('upphone_msg')
    class_error = request.session.get("class_error")
    exsit_error = request.session.get("exsit_msg")
    length_error = request.session.get("length_error")
    none_error = request.session.get("none_error")
    print('喔2')
    print(none_error)
    print(class_error)
    if class_error:
        del request.session['class_error']
    if exsit_error:
        del request.session['exsit_msg']
    if length_error:
        del request.session['length_error']
    if none_error:
        del request.session['none_error']
    print('没有')
    print(msg)
    if msg:
        print('删除')
        del request.session['msg']
    if up_msg:
        del request.session['up_msg']
    if up_msg1:
        del request.session['up_msg1']
    if upphone_msg:
        del request.session['upphone_msg']
    print('当前登陆用户是：{0}'.format(username))
    # template = loader.get_template('work/person.html')
    # Users_id = request.GET.get('Users_id')
    user = UserInfo.objects.filter(username = username)
    phone = [j.phone for j in user]
    image = [j.image for j in user]
    phone = phone[0]
    image = image[0]
    print(phone[0])
    print(image)
    if image == '':
        image = 'touxiang.jpg'
    video = Users.objects.filter(username = username)
    num = Users.objects.filter(username = username,status = 1)
    num2 = Users.objects.filter(username = username,status = 2)
    num1 = Users.objects.filter(username = username,status = 3)
    # num = [j.count for j in num]
    num = len(num)
    num1 = len(num1)
    num2 = len(num2)
    print(num)
    url = [j.headimg for j in video]
    print(url)
    # context = RequestContext(request, {'username': username,'phone':phone[0],'url':url})
    Users_list = Users.objects.filter(username = username,status = 2).order_by('-uptime')
    print(Users_list)
    paginator = Paginator(Users_list, 9)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list1 = paginator.page(current_num)
    except EmptyPage:
        Users_list1 = paginator.page(4)  # 当你输入的page是不存在的时候就会报错
    if paginator.num_pages > 11:  # 如果分页的数目大于11
        if current_num - 5 < 1:  # 你输入的值
            pageRange = range(1, 11)  # 按钮数
        elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
            pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
        else:
            pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        pageRange = paginator.page_range  # 正常分配
        # return render(request,'work/test.html',locals())
    # #上传视频
    # if request.method == 'POST':
    #     print('hhh')
    #     # username = request.POST['username']  # 获取username
    #     myfile = request.FILES.get('myfile', None)  # 获取files二进制流，如果没上传为None
    #     if myfile is None:
    #         print('我是谁')
    #     print(myfile)
    #     if myfile:
    #         with open('F:/python project/dj_study/django_test/static/media/{0}'.format(myfile.name), 'wb') as f:
    #             for data in myfile.chunks():
    #                 f.write(data)
    #             user = Users()  # 存储到数据库，img为存储的文件名，使用时，加上上传文件路径即可
    #             user.username = username
    #             user.headimg = myfile.name
    #             user.uptime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #             user.save()
    #             return HttpResponseRedirect("/work/person/")
    #

    return render_to_response('work/person.html',locals())

@csrf_exempt
def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        print(userform)
        if userform.is_valid():
            print('进来了')
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            password1 = userform.cleaned_data['password1']
            phone = userform.cleaned_data['phone']
            ret = re.match(r"^1[35678]\d{9}$", phone)
            if ret:
                user = UserInfo.objects.filter(username=username)
                userinfo = UserInfo()
                userinfo.username = username
                userinfo.password = password
                userinfo.phone = phone
                print(user)
                if password != password1:
                    return render_to_response('work/register.html',{'pwd_error':'两次密码不一致！请重新输入'})
                if user:
                    return render_to_response('work/register.html', {'error': "注册失败！用户名已存在，请重新输入"})
                # userinfo.objects.create(username=username, password=password, phone=phone)
                else:
                    userinfo.save()
                request.session['register_msg'] = '注册成功！'
                return HttpResponseRedirect('/work/home', {'username': username})
            else:
                return render_to_response('work/register.html',{'phone_error':'手机号码格式错误！'})
        else:
            return render_to_response('work/register.html',{'null_error':'用户名、密码、手机后不能为空！'})
    else:
        userform = UserForm()
        return render_to_response('work/register.html' , {'userForm':userform})

@csrf_exempt
def register1(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        url = request.GET.get('url')
        print(userform)
        if userform.is_valid():
            print('进来了')
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            password1 = userform.cleaned_data['password1']
            phone = userform.cleaned_data['phone']
            ret = re.match(r"^1[35678]\d{9}$", phone)
            if ret:
                user = UserInfo.objects.filter(username=username)
                userinfo = UserInfo()
                userinfo.username = username
                userinfo.password = password
                userinfo.phone = phone
                print(user)
                if password != password1:
                    return render_to_response('work/register.html', {'pwd_error': '两次密码不一致！请重新输入'})
                if user:
                    return render_to_response('work/register.html', {'error': "注册失败！用户名已存在，请重新输入"})
                # userinfo.objects.create(username=username, password=password, phone=phone)
                else:
                    userinfo.save()
                request.session['register_msg1'] = '注册成功！'
                return HttpResponseRedirect('/work/playpage?url='+url, {'userform': userform})
            else:
                return render_to_response('work/register.html', {'phone_error': '手机号码格式错误！'})
        else:
            return render_to_response('work/register.html',{'null_error':'用户名、密码、手机后不能为空！'})
    else:
        userform = UserForm()
        return render_to_response('work/register.html' , {'userForm':userform})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        print('欢迎')
        userform = Login(request.POST)
        # print(userform)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            print(username+password)
            user = UserInfo.objects.filter(username=username, password=password)
            status = UserInfo.objects.values('authority').get(username=username)
            status = status['authority']
            print(status)
            print('你好')
            if user:
                request.session['username'] = username  # 使用session来保存用户登录信息
                request.session['login_msg'] = '登陆成功！'  # 使用session来保存用户登录信息
                # response.set_cookie('name',username_get) #使用response（用户自己电脑）保存的cookie来验证用户登录
                if status == 1:
                    print('普通用户')
                    return HttpResponseRedirect('/work/home', {'userform': userform})
                else:
                    print('管理员')
                    return HttpResponseRedirect('/work/administrator')
            else:
                return render_to_response('work/login.html',{'login_error':'用户或者密码错误，请重新输入！'})
        else:
            return render_to_response('work/login.html',{'null_error':'用户、密码不能为空！'})
    else:
        print('报错')
        userform = UserForm()
        return render_to_response('work/login.html', {'userform': userform})

@csrf_exempt
def login1(request):
    if request.method == 'POST':
        print('欢迎')
        userform = Login(request.POST)
        url = request.GET.get('url')
        # print(userform)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            print(username+password)
            user = UserInfo.objects.filter(username=username, password=password)
            print('你好')
            if user:
                request.session['username'] = username  # 使用session来保存用户登录信息
                request.session['login_msg1'] = '登陆成功！'  # 使用session来保存用户登录信息
                # response.set_cookie('name',username_get) #使用response（用户自己电脑）保存的cookie来验证用户登录
                return HttpResponseRedirect('/work/playpage?url='+url, {'userform': userform})
            else:
                return render_to_response('work/login.html',{'login_error':'用户或者密码错误，请重新输入！'})
        else:
            return render_to_response('work/login.html',{'null_error':'用户、密码不能为空！'})
    else:
        print('报错')
        userform = UserForm()
        return render_to_response('work/login.html', {'userform': userform})

@csrf_exempt
def uppassword(request):
    username = request.session.get("username")
    if request.method == 'POST':
        print('欢迎')
        userform = Uppassword(request.POST)
        # print(userform)
        if userform.is_valid():
            phone = userform.cleaned_data['phone']
            password = userform.cleaned_data['password']
            password1 = userform.cleaned_data['password1']
            print(username+password)
            user = UserInfo.objects.filter(username=username, phone=phone)
            print('你好')
            if user:
                # request.session['username'] = username  # 使用session来保存用户登录信息
                # response.set_cookie('name',username_get) #使用response（用户自己电脑）保存的cookie来验证用户登录
                if password == password1:
                    UserInfo.objects.filter(username=username).update(password=password)
                    request.session['uppwd_msg'] = '修改成功！'
                    return HttpResponseRedirect('/work/logout', {'userform': userform})
                else:
                    return render_to_response('work/uppassword.html',{'up_error':'两次密码不一致,请重新输入！','username': username})
            else:
                return render_to_response('work/uppassword.html',{'phone_error':'手机号码错误，请重新输入！','username': username})
        else:
            return render_to_response('work/uppassword.html',{'null_error':'手机号码、密码不能为空！','username': username})
    else:
        print('报错')
        userform = UserForm()
        print(username)
        return render_to_response('work/uppassword.html', {'username': username})

@csrf_exempt
def upphone(request):
    username = request.session.get("username")
    if request.method == 'POST':
        print('欢迎')
        userform = Upphone(request.POST)
        # print(userform)
        if userform.is_valid():
            phone = userform.cleaned_data['phone']
            password = userform.cleaned_data['password']
            print(username+password)
            user = UserInfo.objects.filter(username=username, password=password)
            print('你好')
            if user:
                # request.session['username'] = username  # 使用session来保存用户登录信息
                # response.set_cookie('name',username_get) #使用response（用户自己电脑）保存的cookie来验证用户登录
                ret = re.match(r"^1[35678]\d{9}$", phone)
                if ret:
                    UserInfo.objects.filter(username=username).update(phone=phone)
                    request.session['upphone_msg'] = '修改手机号码成功！'
                    return HttpResponseRedirect('/work/person', {'userform': userform})
                else:
                    return render_to_response('work/upphone.html',{'phone_error':'手机号码格式错误！','username': username})
            else:
                return render_to_response('work/upphone.html',{'pwd_error':'密码错误！','username': username})
        else:
            return render_to_response('work/upphone.html',{'null_error':'手机号码、密码不能为空！','username': username})
    else:
        print('报错')
        userform = UserForm()
        print(username)
        return render_to_response('work/upphone.html', {'username': username})

def delete(request):
    username = request.session.get("username")
    videoname = request.GET.get("filename")
    s = Users.objects.filter(username = username,headimg = videoname)
    print('晋')
    print(videoname)
    print(s)
    if s:
        print('san')
        Users.objects.filter(username=username, headimg=videoname).delete()
        request.session['msg'] = '删除成功！'
        return HttpResponseRedirect("/work/person",{'del':'删除成功！'})
    print('no')
    return render_to_response("work/person.html",{'del':'删除失败！'})

def delete1(request):
    username = request.session.get("username")
    videoname = request.GET.get("filename")
    s = Users.objects.filter(username = username,headimg = videoname)
    print('晋')
    print(videoname)
    print(s)
    if s:
        print('san')
        Users.objects.filter(username=username, headimg=videoname).delete()
        request.session['msg'] = '取消成功！'
        return HttpResponseRedirect("/work/review",{'del':'取消成功！'})
    print('no')
    return render_to_response("work/person.html",{'del':'删除失败！'})

def ll(request):
    username = request.session.get("username")
    videoname = request.GET.get("filename")
    s = Users.objects.filter(username = username,headimg = videoname)
    print('晋')
    print(videoname)
    print(s)
    if s:
        print('san')
        Users.objects.filter(username=username, headimg=videoname).delete()
        request.session['msg'] = '删除成功！'
        return HttpResponseRedirect("/work/refuse",{'del':'取消成功！'})
    print('no')
    return render_to_response("work/person.html",{'del':'删除失败！'})

def review(request):
    username = request.session['username']
    msg = request.session.get('msg')
    up_msg = request.session.get('up_msg')
    up_msg1 = request.session.get('up_msg1')
    upphone_msg = request.session.get('upphone_msg')
    class_error = request.session.get("class_error")
    exsit_error = request.session.get("exsit_msg")
    length_error = request.session.get("length_error")
    none_error = request.session.get("none_error")
    print(class_error)
    if class_error:
        del request.session['class_error']
    if exsit_error:
        del request.session['exsit_msg']
    if length_error:
        del request.session['length_error']
    if none_error:
        del request.session['none_error']
    print('没有')
    print(msg)
    if msg:
        print('删除')
        del request.session['msg']
    if up_msg:
        del request.session['up_msg']
    if up_msg1:
        del request.session['up_msg1']
    if upphone_msg:
        del request.session['upphone_msg']
    print('当前登陆用户是：{0}'.format(username))
    # template = loader.get_template('work/person.html')
    # Users_id = request.GET.get('Users_id')
    user = UserInfo.objects.filter(username=username)
    phone = [j.phone for j in user]
    image = [j.image for j in user]
    phone = phone[0]
    image = image[0]
    print(phone[0])
    print(image)
    if image == '':
        image = 'touxiang.jpg'
    video = Users.objects.filter(username=username)
    num = Users.objects.filter(username=username, status=1)
    num2 = Users.objects.filter(username=username, status=2)
    num1 = Users.objects.filter(username=username, status=3)
    # num = [j.count for j in num]
    num = len(num)
    num1 = len(num1)
    num2 = len(num2)
    print(num)
    url = [j.headimg for j in video]
    print(url)
    # context = RequestContext(request, {'username': username,'phone':phone[0],'url':url})
    Users_list = Users.objects.filter(username=username, status=1).order_by('-uptime')
    print(Users_list)
    dispaly = 'none'
    paginator = Paginator(Users_list, 9)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list2 = paginator.page(current_num)
    except EmptyPage:
        Users_list2 = paginator.page(4)  # 当你输入的page是不存在的时候就会报错
    if paginator.num_pages > 11:  # 如果分页的数目大于11
        if current_num - 5 < 1:  # 你输入的值
            pageRange = range(1, 11)  # 按钮数
        elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
            pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
        else:
            pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        pageRange = paginator.page_range  # 正常分配


    return render_to_response('work/person.html', locals())

def refuse(request):
    username = request.session['username']
    msg = request.session.get('msg')
    up_msg = request.session.get('up_msg')
    up_msg1 = request.session.get('up_msg1')
    upphone_msg = request.session.get('upphone_msg')
    class_error = request.session.get("class_error")
    exsit_error = request.session.get("exsit_msg")
    length_error = request.session.get("length_error")
    none_error = request.session.get("none_error")
    print(class_error)
    if class_error:
        del request.session['class_error']
    if exsit_error:
        del request.session['exsit_msg']
    if length_error:
        del request.session['length_error']
    if none_error:
        del request.session['none_error']
    print('没有')
    print(msg)
    if msg:
        print('删除')
        del request.session['msg']
    if up_msg:
        del request.session['up_msg']
    if up_msg1:
        del request.session['up_msg1']
    if upphone_msg:
        del request.session['upphone_msg']
    print('当前登陆用户是：{0}'.format(username))
    # template = loader.get_template('work/person.html')
    # Users_id = request.GET.get('Users_id')
    user = UserInfo.objects.filter(username=username)
    phone = [j.phone for j in user]
    image = [j.image for j in user]
    phone = phone[0]
    image = image[0]
    print(phone[0])
    print(image)
    if image == '':
        image = 'touxiang.jpg'
    video = Users.objects.filter(username=username)
    num1 = Users.objects.filter(username=username, status=3)
    num2 = Users.objects.filter(username=username, status=2)
    num = Users.objects.filter(username=username, status=1)
    # num = [j.count for j in num]
    num1 = len(num1)
    num2 = len(num2)
    num = len(num)
    print(num1)
    url = [j.headimg for j in video]
    dispaly1 = 'none'
    print(url)
    print('在这里')
    print(dispaly1)
    # context = RequestContext(request, {'username': username,'phone':phone[0],'url':url})
    Users_list = Users.objects.filter(username=username, status=3).order_by('-uptime')
    print(Users_list)
    paginator = Paginator(Users_list, 9)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list3 = paginator.page(current_num)
    except EmptyPage:
        Users_list3 = paginator.page(4)  # 当你输入的page是不存在的时候就会报错
    if paginator.num_pages > 11:  # 如果分页的数目大于11
        if current_num - 5 < 1:  # 你输入的值
            pageRange = range(1, 11)  # 按钮数
        elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
            pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
        else:
            pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        pageRange = paginator.page_range  # 正常分配


    return render_to_response('work/person.html', locals())

@csrf_exempt
def administrator(request):
    username = request.session['username']
    msg = request.session.get('msg')
    up_msg = request.session.get('up_msg')
    up_msg1 = request.session.get('up_msg1')
    upphone_msg = request.session.get('upphone_msg')
    class_error = request.session.get("class_error")
    exsit_error = request.session.get("exsit_msg")
    length_error = request.session.get("length_error")
    print(class_error)
    if class_error:
        del request.session['class_error']
    if exsit_error:
        del request.session['exsit_msg']
    if length_error:
        del request.session['length_error']
    print('没有')
    print(msg)
    if msg:
        print('删除')
        del request.session['msg']
    if up_msg:
        del request.session['up_msg']
    if up_msg1:
        del request.session['up_msg1']
    if upphone_msg:
        del request.session['upphone_msg']
    print('当前登陆用户是：{0}'.format(username))
    # template = loader.get_template('work/person.html')
    # Users_id = request.GET.get('Users_id')
    user = UserInfo.objects.filter(username = username)
    phone = [j.phone for j in user]
    image = [j.image for j in user]
    phone = phone[0]
    image = image[0]
    print(phone[0])
    print(image)
    if image == '':
        image = 'touxiang.jpg'
    video = Users.objects.filter(username = username)
    num = Users.objects.filter(status = 1)
    num1 = Users.objects.filter(status = 3)
    # num = [j.count for j in num]
    num = len(num)
    num1 = len(num1)
    print(num)
    url = [j.headimg for j in video]
    print(url)
    # context = RequestContext(request, {'username': username,'phone':phone[0],'url':url})
    Users_list = Users.objects.filter(status = 1).order_by('-uptime')
    print(Users_list)
    paginator = Paginator(Users_list, 9)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list1 = paginator.page(current_num)
    except EmptyPage:
        Users_list1 = paginator.page(4)  # 当你输入的page是不存在的时候就会报错
    if paginator.num_pages > 11:  # 如果分页的数目大于11
        if current_num - 5 < 1:  # 你输入的值
            pageRange = range(1, 11)  # 按钮数
        elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
            pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
        else:
            pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        pageRange = paginator.page_range  # 正常分配

    return render_to_response('work/admin.html',locals())

def b_pass(request):
    username = request.GET.get('username')
    filename = request.GET.get('filename')
    up = Users.objects.filter(username=username,headimg=filename).update(status=2)
    if up:
        return HttpResponseRedirect('/work/administrator')

def b_refuse(request):
    username = request.GET.get('username')
    filename = request.GET.get('filename')
    up = Users.objects.filter(username=username, headimg=filename).update(status=3)
    if up:
        return HttpResponseRedirect('/work/administrator')

def c_refuse(request):
    username = request.session['username']
    msg = request.session.get('msg')
    up_msg = request.session.get('up_msg')
    up_msg1 = request.session.get('up_msg1')
    upphone_msg = request.session.get('upphone_msg')
    class_error = request.session.get("class_error")
    exsit_error = request.session.get("exsit_msg")
    length_error = request.session.get("length_error")
    print(class_error)
    if class_error:
        del request.session['class_error']
    if exsit_error:
        del request.session['exsit_msg']
    if length_error:
        del request.session['length_error']
    print('没有')
    print(msg)
    if msg:
        print('删除')
        del request.session['msg']
    if up_msg:
        del request.session['up_msg']
    if up_msg1:
        del request.session['up_msg1']
    if upphone_msg:
        del request.session['upphone_msg']
    print('当前登陆用户是：{0}'.format(username))
    # template = loader.get_template('work/person.html')
    # Users_id = request.GET.get('Users_id')
    user = UserInfo.objects.filter(username=username)
    phone = [j.phone for j in user]
    image = [j.image for j in user]
    phone = phone[0]
    image = image[0]
    print(phone[0])
    print(image)
    if image == '':
        image = 'touxiang.jpg'
    video = Users.objects.filter(username=username)
    num1 = Users.objects.filter(status=3)
    num = Users.objects.filter(status=1)
    # num = [j.count for j in num]
    num1 = len(num1)
    num = len(num)
    print(num1)
    url = [j.headimg for j in video]
    dispaly1 = 'none'
    print(url)
    print('在这里')
    print(dispaly1)
    # context = RequestContext(request, {'username': username,'phone':phone[0],'url':url})
    Users_list = Users.objects.filter(status=3).order_by('-uptime')
    print(Users_list)
    paginator = Paginator(Users_list, 9)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        Users_list2 = paginator.page(current_num)
    except EmptyPage:
        Users_list2 = paginator.page(4)  # 当你输入的page是不存在的时候就会报错
    if paginator.num_pages > 11:  # 如果分页的数目大于11
        if current_num - 5 < 1:  # 你输入的值
            pageRange = range(1, 11)  # 按钮数
        elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
            pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数
        else:
            pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        pageRange = paginator.page_range  # 正常分配


    return render_to_response('work/admin.html', locals())