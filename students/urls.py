
from django.contrib import admin
from django.conf import settings
from django.urls import include, path  # For django versions from 2.0 and up



from students_app.views import students_list, hello_world, request_
from teachers.views import run, create_teacher, teachers_list
from groupes.views import Groupe_, create_groupe, groupes_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('students-list/', students_list),
    path('teachers-list/', teachers_list),
    path('groupes-list/', groupes_list),
    path('teachers/', run),
    path('groupes/', Groupe_),
    path('students/', request_),
    path('create-teacher/', create_teacher),
    path('create-groupe/', create_groupe),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),


    ] + urlpatterns