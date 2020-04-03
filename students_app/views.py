from django.shortcuts import render
from django.http import HttpResponse
from students_app.models import Student
from faker import Faker
from random import randint


fake = Faker()

def hello_world(request):
    s = Student.objects.create(first_name=fake.name(), last_name=fake.last_name(), age= randint(20, 70), email =fake.email(), phone=fake.phone_number())
    ss = str(s.id) + '  ' + str(s.first_name) + ' ' + str(s.last_name) + ' ' + str(s.age) + ' ' + str(s.email) + ' ' + str(s.phone)
    return HttpResponse(ss)




