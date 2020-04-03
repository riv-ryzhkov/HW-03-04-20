from django.shortcuts import render
from django.http import HttpResponse
from groupes.models import Groupe



def Groupe_(request):
    g = Groupe.objects.create(name='PGS-2020', head='Dmitry', email='rty@gmail.com', phone='76565')
    return HttpResponse(g.name)

