from django.urls import path
from app2.views import *
app_name='somethinggg'
urlpatterns=[
    path('job/',job,name='job'),
]