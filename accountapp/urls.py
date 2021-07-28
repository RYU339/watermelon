from django.urls import path

from accountapp.views import tahlee

app_name = 'accountapp'

urlpatterns = [
    path('tahlee/', tahlee, name='tahlee')
]