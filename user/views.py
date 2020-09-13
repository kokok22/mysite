from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import user.models


def joinform(request):
    return render(request,'user/joinform.html')


def loginform(request):
    return render(request, 'user/loginform.html')


def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/main')


def updateform(request):
    no = request.session['authuser']['no']
    print(no)
    result = user.models.fetchonebyteno(no)
    print(result)
    return render(request,'user/updateform.html',result)

def update(request):
    no = request.session['authuser']['no']
    name = request.POST['name']
    password = request.POST['password']
    gender = request.POST['gender']

    user.models.update(no, name, password,gender)

    request.session['authuser'] = {'no':no, 'name':name}

    return HttpResponseRedirect('/user/updateform')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def join(request):
    # name을 확인하는 것이다.
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    user.models.insert(name, email, password, gender)

    return HttpResponseRedirect('/user/joinsuccess')


def login(request):
    email = request.POST['email']
    password = request.POST['password']

    result = user.models.fetchone(email, password)
    if result is None:
        return HttpResponseRedirect('/user/loginform?result=fail')


    request.session['authuser'] = result                    # 로그인 했다는 정보를 저장하는 것이다.

    return HttpResponseRedirect('/main')