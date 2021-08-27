from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel


@login_required
def tahlee(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')

        new_model = NewModel()  # (): NewModel에서 나온 새로운 객체가 new_model로 저장됨
        new_model.text = temp
        new_model.save()

        return HttpResponseRedirect(reverse('accountapp:tahlee'))
    # CONTEXT = 맥락, 데이터 꾸러미, test: 이름, post method: 내용물 text를 html 안에 넣어서 보낼 것
    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/tahlee.html', context={'data_list': data_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:tahlee')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

has_ownership=[login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:tahlee')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:tahlee')
    template_name = 'accountapp/delete.html'