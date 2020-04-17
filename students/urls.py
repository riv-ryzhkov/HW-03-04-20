
from django.contrib import admin
from django.conf import settings
from django.urls import include, path  # For django versions from 2.0 and up



from students_app.views import students_list, hello_world, request_
from teachers.views import run, create_teacher, teachers_list, teacher_edit, feedback, email
from groupes.views import Groupe_, create_groupe, groupes_list, groupe_edit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('students-list/', students_list, name='students-list'),
    path('teachers-list/', teachers_list, name='teachers-list'),
    path('groupes-list/', groupes_list, name='groupes-list'),
    path('teachers/', run, name='teachers'),
    path('groupes/', Groupe_, name='groupes'),
    path('students/', request_, name='students'),
    path('create-teacher/', create_teacher, name='create-teacher'),
    path('feedback/', feedback, name='feedback'),
    path('email/', email, name='email'),
    path('create-groupe/', create_groupe, name='create-groupe'),
    path('teacher-edit/<int:pk>/', teacher_edit, name='teacher-edit'),
    path('groupe-edit/<int:pk>/', groupe_edit, name='groupe-edit'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),


    ] + urlpatterns