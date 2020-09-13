from django.shortcuts import render
from django.http import HttpResponseRedirect
import guestbook.models

# Create your views here.

def index(request):
    result = guestbook.models.fetchlist()
    data = {'guestbooklist':result}
    return render(request,'guestbook/index.html',data)


def deleteform(request):
    return render(request,'guestbook/deleteform.html')


def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    guestbook.models.delete(no, password)

    return HttpResponseRedirect('/guestbook')


def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    guestbook.models.insert(name, password, message)

    return HttpResponseRedirect('/guestbook')
