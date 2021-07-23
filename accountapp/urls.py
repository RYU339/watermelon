from django.urls import path

from accountapp.views import watermelon

app_name = 'accountapp'

urlpatterns = [
    path('watermelon/', watermelon, name='watermelon')
]