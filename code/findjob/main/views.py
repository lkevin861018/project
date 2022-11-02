from asyncio.windows_events import NULL
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from main.models import Dreamreal
from django.core.mail import send_mail
import re

# Create your views here.


def confirm(request):
    res = send_mail("confirm mail", "<a href='127.0.0.1:8000/main/complete'>點擊認證</a><br>",
                    "kevinliang1018@gmail.com", ['kevinliang1018@gmail.com'])
    return HttpResponse('%s' % res)


def signIn(request):
    if request.method == 'POST':
        lastname = request.POST['last_name']
        firstname = request.POST['first_name']
        pid = request.POST['pid']
        email = request.POST['email']
        passwd = request.POST['passwd']

        try:
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

                dreamreal = Dreamreal(
                    lastname=str(lastname),
                    firstname=str(firstname),
                    pid=str(pid),
                    email=str(email),
                    passwd=str(passwd)
                )

                dreamreal.save()
                messages.add_message(
                    request, messages.INFO, '註冊成功')
                return redirect('login')
        except:
            messages.add_message(
                request, messages.INFO, '身分證或email已註冊過!')
            return render(request, 'signIn.html')
    else:
        return render(request, 'signIn.html')

    # # Update
    # dreamreal = Dreamreal(
    #     website="www.google.com",
    #     mail="alvin@google.com.com",
    #     name="alvin",
    #     phonenumber="0911222444"
    # )

    # dreamreal.save()
    # res += 'Updating entry<br>'

    # dreamreal = Dreamreal.objects.get(name='alvin')
    # dreamreal.name = 'mary'
    # dreamreal.save()

    # return HttpResponse(res)


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

    # def loginProcess(request):
    #     name = request.POST('user')
    #     passwd = request.POST('passwd')

    #     try:
    #         user = account.objects.get(userName=name)
    #         if user.passwd == passwd:
    #             return HttpResponse('success')
    #         else:
    #             return HttpResponse('fail')
    #     except:
    #         return HttpResponse('no account')
