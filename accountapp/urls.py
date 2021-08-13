from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import tahlee, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('tahlee/', tahlee, name='tahlee'),
    path('create/', AccountCreateView.as_view(), name='create'),

]