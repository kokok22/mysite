from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import board.models


def index(request):
    results = board.models.fetchlist()

    page, bound = paging(request)

    data = {'boardlist': results, 'page': page, 'range': bound}

    return render(request, 'board/list.html',data)


def paging(request):
    try:
        page = int(request.GET['page'])
    except:
        page = 1

    if page <= 2:
        bound = range(1,6)
    else:
        bound = range(page-2,page+3)

    return page, bound


def writeform(request):
    try:
        no = request.GET['no']
    except:
        no = -1
    data = {'no': no}
    return render(request, 'board/write.html',data)


def write(request):
    title = request.POST['title']
    user_no = request.session['authuser']['no']
    content = request.POST['content']

    if request.GET['no'] != '-1':
        result = board.models.fetchno( request.GET['no'])
        g_no = result['g_no']
        o_no = result['o_no'] + 1
        depth = result['depth'] + 1

    else:
        g_no = board.models.selectg_no()
        if g_no is None:
            g_no =1
        else:
            g_no = g_no['g_no']+1
        o_no = 1
        depth = 1

    board.models.insert(title, content, user_no, g_no, o_no, depth)

    return HttpResponseRedirect('/board')


def view(request):
    no = request.GET['no']
    results = board.models.fetchno(no)
    board.models.updateview(no)
    data = {'result' : results}
    return render(request, 'board/view.html', data)


def modifyform(request):
    return render(request, 'board/modify.html')


def modify(request):
    no = request.POST['no']
    title = request.POST['title']
    content = request.POST['content']

    board.models.update(no,title, content)

    return HttpResponseRedirect('view?no={}'.format(no))


def delete(request):
    no = request.GET['no']
    board.models.delete(no)

    return HttpResponseRedirect('/board')