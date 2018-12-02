from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import random
import hashlib
from .models import Diary, Log, AdminDiary, student
from collections import defaultdict


def logging(func):
    def wraper(request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        log = Log()
        try:
            username = request.META.get('USERNAME')
            path = request.path
            log.ip = ip
            log.name = username
            log.url = path
            log.save()
        except:
            log.ip = 'wrong'
            log.name = 'wrong'
            log.url = 'wrong'
            log.save()

        return func(request)
    return wraper


def jurisdiction(func):
    """权限过滤，用于分享权限过滤"""
    def wraper(request, dia):
        try:
            a = AdminDiary.objects.get(identification_id=dia)
            session = request.session['share_password'] if 'share_password' in request.session else ''
            print('session==', session)
            if a.share or session == '1996Chan':
                return func(request, dia)
            else:
                context = {'title': 'No Power', 'content': 'You Have No Power To have This Text', 'next': dia}
                return render(request, 'jurisdiction_show.html', context)
        except:
            context = {'title': 'accident', 'content': 'an accident was happend OR you have no power hahahaha', 'next': dia}
            return render(request, 'jurisdiction_show.html', context)

    return wraper


def add_power(request):
    next = request.GET.get('next')
    print('next=', next)
    if request.method == 'POST':
        password = request.POST['share_password']
        print('password', password)
        if password == '1996Chan':
            request.session['share_password'] = password
            request.session.set_expiry(0)
            return HttpResponseRedirect('detail/'+next)
        else:
            context = {'title': 'accident', 'content': 'an accident was happend!'}
            return render(request, 'jurisdiction_show.html', context)


@logging
def index(request):
    con = Diary.objects.all().values().order_by('-date', '-date_time')
    p = defaultdict(list)
    for i in con:
        if i['text'] is not None and i['identification_id'] not in p:
            p[i['identification_id']].append(i)
    return render(request, 'index.html', {'content': dict(p)})


def write(request):
    if request.method == 'POST':
        rand = random.random()
        sha = hashlib.sha1()
        sha.update(str(rand).encode('utf-8'))
        sign = sha.hexdigest()
        n = 1
        f = True
        for i in request.POST:
            if 'text' in i:
                if f:
                    a = AdminDiary(header=request.POST['title'], text=request.POST[i], share=0, identification_id=sign)
                    a.save()
                    f = False
                d = Diary()
                d.identification_id = sign
                d.header = request.POST['title']
                d.text = request.POST[i]
                # d.date = time.time()
                d.order_num = n
                d.user_id = '1123'
                d.save()
                n += 1

        for i in request.FILES:
            if 'pic' in i:
                d = Diary()
                d.identification_id = sign
                d.header = request.POST['title']
                d.images = request.FILES[i]
                d.order_num = n
                d.user_id = '1123'
                d.save()
                n += 1

        return render(request, 'write.html', {})
    else:
        return render(request, 'write.html', {})


@jurisdiction
def detail(request, dia):
    a = Diary.objects.filter(identification_id=dia).values()
    lis = {}
    title = ""
    date = ""
    for i in a:
        print(i['images'])
        title = i['header']
        date = i['date']
        lis[i['order_num']] = i
    key = lis.keys()
    key = sorted(key)
    lis = map(lis.get, key)

    return render(request, 'detail.html', {'title': title, 'date': date, 'content': lis})


def search(request):
    return render(request, 'infor.html', {})


def information(request):
    id = request.POST.get('id')
    print(id)
    try:
        stu = student.objects.get(number=id)
    except Exception as e:
        stu = None
    return render(request, 'infor2.html', {'stu': stu})


def save_information(request):
    if request.is_ajax():
        id = request.POST.get('ID')
        eng = request.POST.get('eng')
        # print(id, eng)
        a = student.objects.filter(number=id).values('number')
        print(a)
        if not a:
            return HttpResponse('2')
        else:
            return HttpResponse('succ')
