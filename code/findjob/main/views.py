from asyncio.windows_events import NULL
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from main.models import Dreamreal
from django.core.mail import send_mail
import re
import string
import random

# Create your views here.

complete = []
complete_key = ''.join(random.choice(string.ascii_letters + string.digits)
                       for _ in range(10))


def confirm(request):
    global complete_key
    try:
        if request.GET.get('k') == complete_key:
            dreamreal = Dreamreal(
                lastname=complete[0],
                firstname=complete[1],
                pid=complete[2],
                email=complete[3],
                passwd=complete[4]
            )

            dreamreal.save()
            messages.add_message(
                request, messages.INFO, '註冊成功')
            return redirect('login')
        else:
            messages.add_message(
                request, messages.INFO, '驗證錯誤，請重新註冊!')
            return render(request, 'signIn.html')
    except:
        messages.add_message(
            request, messages.INFO, '帳號已驗證過!')
        return render(request, 'signIn.html')


def signIn(request):
    if request.method == 'POST':
        lastname = request.POST['last_name']
        firstname = request.POST['first_name']
        pid = request.POST['pid']
        email = request.POST['email']
        passwd = request.POST['passwd']
        try:
            Dreamreal.objects.get(pid=pid) == None
            Dreamreal.objects.get(email=email) == None
            account_exist = 1
        except:
            account_exist = 0

        if account_exist:
            if '' in [lastname, firstname, pid, email, passwd]:
                messages.add_message(
                    request, messages.INFO, '資料不完整請重新輸入!')
                return render(request, 'signIn.html')
            elif None == re.search(r'[A-Z]{1}\d{9}', str(pid)):
                messages.add_message(
                    request, messages.INFO, '身分格式錯誤請重新輸入!')
                return render(request, 'signIn.html')
            elif None == re.search(r"\w+@\w+\.\w+", str(email)):
                messages.add_message(
                    request, messages.INFO, '信箱格式錯誤請重新輸入!')
                return render(request, 'signIn.html')
            else:
                # sendSimpleEmail(request, email)
                global complete_key
                lastname = str(lastname)
                firstname = str(firstname)
                pid = str(pid)
                email = str(email)
                passwd = str(passwd)
                send_mail("confirm mail", "進入此連結驗證:http://127.0.0.1:8000/main/confirm?k=%s" % complete_key,
                          "kevinliang1018@gmail.com", [email])

                global complete
                complete = [lastname, firstname, pid, email, passwd]

                return HttpResponse('請至信箱驗證')
        else:
            messages.add_message(
                request, messages.INFO, '身分證或email已註冊過!')
            return render(request, 'signIn.html')
    else:
        return render(request, 'signIn.html')


def login(request):
    if request.method == 'POST':
        if request.session.has_key('account'):
            account = request.session['account']
            passwd = request.session['passwd']
        else:
            account = request.POST['account']
            passwd = request.POST['passwd']

        try:
            try:
                user = Dreamreal.objects.get(pid=account)
                request.session['account'] = user.pid
            except:
                user = Dreamreal.objects.get(email=account)
                request.session['account'] = user.email

            if user.passwd == passwd:
                request.session['passwd'] = user.passwd
                return render(request, 'main.html')
            else:
                messages.add_message(
                    request, messages.INFO, '帳號或密碼錯誤!')
                return render(request, 'login.html')
        except:
            messages.add_message(
                request, messages.INFO, '帳號不存在!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    try:
        del request.session['account']
        del request.session['passwd']
    except:
        pass
    return redirect("login")


def reset(request):
    if request.method == 'POST':
        account = request.POST['account']
        re_pass = request.POST['repass']
        try:
            user = Dreamreal.objects.get(pid=account)
        except:
            user = Dreamreal.objects.get(email=account)

        try:
            if user.passwd == re_pass:
                messages.add_message(
                    request, messages.INFO, '不可與原秘碼相同!')
                return render(request, 'reset.html')
            else:
                user.passwd = re_pass
                user.save()

                messages.add_message(
                    request, messages.INFO, '密碼重設完成!')

                return redirect("login")
        except:
            messages.add_message(
                request, messages.INFO, '非預期錯誤!')
            return render(request, 'reset.html')
