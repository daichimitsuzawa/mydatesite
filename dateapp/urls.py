from django.urls import path
from . import  views

urlpatterns=[
    path('',views.date_list, name='date_list'),
]
