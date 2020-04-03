
from django.contrib import admin
from django.urls import path

from students_app.views import hello_world
from students_app.views import request_
from teachers.views import teacher_
from teachers.views import run
from groupes.views import Groupe_


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('teachers/', run),
    path('groupes/', Groupe_),
    path('students/', request_),

]
