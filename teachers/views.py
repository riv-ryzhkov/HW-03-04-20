from django.shortcuts import render
from django.http import HttpResponse
from teachers.models import Teacher
from groupes.models import Groupe
from students_app.models import Student


def teacher_(request):
    t = Teacher.objects.create(first_name='Ivan', last_name='Petrov', age=32, phone='77686565')
    return HttpResponse(t.first_name + t.last_name + str(t.age))

def clear(request):
    return


def run(request):
    Teacher.objects.all().delete()
    for i in range(5):
        teacher_('')
    tt = 'Teachers = ' + str(Teacher.objects.count()) + '   Students = ' + str(Student.objects.count()) + '   Groups = ' + str(Groupe.objects.count())
    return HttpResponse(tt)

