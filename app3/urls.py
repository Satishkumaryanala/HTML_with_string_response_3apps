from django.urls import path
from app3.views import *

app_name='Third'

urlpatterns=[
    path('app3_first/',app3_first,name='app3_first'),
    path('app3_second/',app3_second,name='app3_second'),
    path('app3_string/',app3_string,name='app3_string'),
]