from django.urls import path
from app1.views import *

app_name='first'

urlpatterns=[
    path('app1_first/',app1_first,name='app1_first'),
    path('app1_second/',app1_second,name='app1_second'),
    path('app1_string/',app1_string,name='app1_string')
]