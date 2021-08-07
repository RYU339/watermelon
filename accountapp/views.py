from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def tahlee(request):

    if request.method == 'POST':
        return render(request, 'accountapp/tahlee.html', context={'text':'POST METHOD'})
    # CONTEXT = 맥락, 데이터 꾸러미, test: 이름, post method: 내용물 text를 html 안에 넣어서 보낼 것
    else:
        return render(request, 'accountapp/tahlee.html', context={'text': 'GET METHOD'})