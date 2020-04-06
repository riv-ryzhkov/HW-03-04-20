from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
from random import randint
from students_app.models import Student
from django.db.models import Q

fake = Faker()

def hello_world(request):
    s = Student.objects.create(first_name=fake.name(), last_name=fake.last_name(), age= randint(20, 70), email =fake.email(), phone=fake.phone_number())
    ss = str(s.id) + '  ' + str(s.first_name) + ' ' + str(s.last_name) + ' ' + str(s.age) + ' ' + str(s.email) + ' ' + str(s.phone)
    return render(request, 'hello.html')


def students_list(request):
    students = Student.objects.all()
    students = students.exclude(age__lt=40)
    q = ~Q(first_name__startswith = 'v')
    q |= Q(first_name__endswith = 'n')
    students = students.filter(q)
    sorting = request.GET.get('order-by')
    if sorting:
        students = students.order_by(*sorting.split(','))


    return render(request, 'students-list.html', {'students': students})



#

def request_(request):
    s = Student.objects.create(first_name=request.GET['name'], last_name=request.GET['last_name'], age=request.GET['age'], email=request.GET['email'], phone=request.GET['phone'])
    for i in str(s.first_name):
        if i.isdigit():
            return HttpResponse('First Name is wron!')
    for i in str(s.last_name):
        if i.isdigit():
            return HttpResponse('Last Name is wron!')
    if str(s.age).isalpha() or int(s.age) < 5 or int(s.age) > 100:
            return HttpResponse('Age is wron!')
    ee = 0
    for i in str(s.email):
        if i == "@":
            ee += 1
    if ee != 1:
        return HttpResponse('Email is wron!')
    if len(s.phone) <= 5 or len(s.phone) > 12:
            return HttpResponse('Phone number is wron!')
    s.save()
    ss = str(s.id) + '  ' + str(s.first_name) + ' ' + str(s.last_name) + ' ' + str(s.age) + ' ' + str(s.email) + ' ' + str(s.phone)
    return HttpResponse(ss)


