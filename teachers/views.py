from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from teachers.models import Teacher
from groupes.models import Groupe
from students_app.models import Student
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

def teacher_(request):
    t = Teacher.objects.create(first_name='Ivan', last_name='Petrov', age=32, phone='77686565', rating=5)
    return render(request, t.first_name + t.last_name + str(t.age))


def clear(request):
    return


def run(request):
    # Teacher.objects.all().delete()
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
            return HttpResponseRedirect(reverse('teachers-list'))
    elif request.method == 'GET':
        form = form_class(initial={'age': 25, 'first_name': 'Ivan', 'email': 'wr@gmail.com', 'phone': '658765', 'last_name': 'Petrov', 'rating': 0})
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

def teacher_edit(request, pk):
    from teachers.forms import TeacherForm
    from django.http import Http404
    from teachers.models import Teacher
    form_class = TeacherForm

    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        raise Http404



    if request.method == 'POST':
        form = form_class(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers-list'))
    elif request.method == 'GET':
        form = form_class(instance=teacher)
    return render(request, 'teacher-edit.html', {'form': form})


def feedback(request):
    from teachers.forms import Feedback
    form_class = Feedback

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('feedback'))
    elif request.method == 'GET':
        form = form_class()
    return render(request, 'feedback.html', {'form': form})


def email(request):
    from teachers.forms import Email
    form_class = Email

    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['riv.django@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )


    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('feedback'))
    elif request.method == 'GET':
        form = form_class()
    return render(request, 'email.html', {'form': form})

