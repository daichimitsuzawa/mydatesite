from .models import Search, Table
from django.shortcuts import render


def date_list(request):
    return render (request, 'dateapp/date.html',{})


def maleNumber(request):
    template_male_name = "date.html"
    template_male_text="male"
    context={"male_text:" : template_male_text}
    return render(request,template_male_name,context)


def femaleNumber(request):
    template_female_name = "date.html"
    template_female_text="female"
    context={"female_text:" : template_female_text}
    return render(request,template_female_name,context)

def situationOfDate(request):
    template_situation_name="date.html"
    template_situation_text="Situation"
    context={"situation_text" : template_situation_text}
    return render (request,template_situation_name,context)



