from .models import Search, Table
from django.shortcuts import render


def date_list(request):
    return render (request, 'dateapp/date.html',{})






