from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from main.models import Dreamreal
from django.core.mail import send_mail
import re

# Create your views here.


# def sendSimpleEmail(request, email):
#     res = send_mail("confirm mail", "<a href='/main/confirm'>點擊認證</a><br>",
#                     "kevinliang1018@gmail.com", email)
#     return HttpResponse('%s' % res)


# def confirm(request):
#     dreamreal = Dreamreal(
#         lastname=str(info[0]),
#         firstname=str(info[1]),
#         pid=str(info[2]),
#         email=str(info[3]),
#         passwd=str(info[4])
#     )
#     dreamreal.save()
#     messages.add_message(
#         request, messages.INFO, '註冊成功')
#     return render(request, 'login.html')


def signIn(request):
    return render(request, 'signIn.html')


info = []


def postsignIn(request):
    if request.method == 'POST':
        lastname = request.POST['last_name']
        firstname = request.POST['first_name']
        pid = request.POST['pid']
        email = request.POST['email']
        passwd = request.POST['passwd']
        global info
        info = [lastname, firstname, pid, email, passwd]

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
                return render(request, 'login.html')
                # return HttpResponse('請至信箱認證!')
        except:
            messages.add_message(
                request, messages.INFO, '身分證或email已註冊過!')
            return render(request, 'signIn.html')

    # # Read ALL entries
    # objects = Dreamreal.objects.all()
    # res = 'Printing all Dreamreal entries in the DB : <br>'

    # for elt in objects:
    #     res += elt.name + "<br>"

    # # Read a specific entry:
    # sorex = Dreamreal.objects.get(name="alvin")
    # res += 'Printing One entry <br>'
    # res += sorex.name

    # # Delete an entry
    # res += '<br> Deleting an entry <br>'
    # sorex.delete()

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


# def login(request):
#     if request.method == 'POST':
#         name = request.POST['user']
#         passwd = request.POST['passwd']

#         try:
#             user = account.objects.get(userName=name)
#             if user.passwd == passwd:
#                 return HttpResponse('success')
#             else:
#                 return HttpResponse('fail')
#         except:
#             return HttpResponse('no account')
#     else:
#         return render(request, 'login.html')


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
