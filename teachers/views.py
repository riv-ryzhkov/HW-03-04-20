from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from teachers.models import Teacher
from groupes.models import Groupe
from students_app.models import Student


def teacher_(request):
    t = Teacher.objects.create(first_name='Ivan', last_name='Petrov', age=32, phone='77686565')
    return render(request, t.first_name + t.last_name + str(t.age))


def clear(request):
    return


def run(request):
    Teacher.objects.all().delete()
    for i in range(5):
        teacher_('')
    tt = 'Teachers = ' + str(Teacher.objects.count()) + '   Students = ' + str(Student.objects.count()) + '   Groups = ' + str(Groupe.objects.count())
    return HttpResponse(tt)

def create_teacher(request):
    from teachers.forms import TeacherForm
    form_class = TeacherForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers-list/')
    elif request.method == 'GET':
        form = form_class()
    return render(request, 'teacher-create.html', {'create_form': form, 'one': 'Teacher'})


def teachers_list(request):
    teachers = Teacher.objects.all()

    age_to_filter = request.GET.get('age')
    name_to_filter = request.GET.get('ln_start')
    if age_to_filter:
        teachers = teachers.filter(age__lte=age_to_filter)

    if age_to_filter:
        teachers = teachers.filter(last_name__startswith=name_to_filter)

    sorting = request.GET.get('order-by')
    if sorting:
        teachers = teachers.order_by(*sorting.split(','))

    return render(request, 'teachers-list.html', {'teachers': teachers})