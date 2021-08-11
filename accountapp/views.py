from django.shortcuts import render

# Create your views here.
from accountapp.models import NewModel


def tahlee(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')

        new_model = NewModel()  # (): NewModel에서 나온 새로운 객체가 new_model로 저장됨
        new_model.text = temp
        new_model.save()

        return render(request, 'accountapp/tahlee.html', context={'tahlee_output': new_model})
    # CONTEXT = 맥락, 데이터 꾸러미, test: 이름, post method: 내용물 text를 html 안에 넣어서 보낼 것
    else:
        return render(request, 'accountapp/tahlee.html', context={'text': 'GET METHOD'})