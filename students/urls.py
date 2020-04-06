
from django.contrib import admin
from django.conf import settings
from django.urls import include, path  # For django versions from 2.0 and up



from students_app.views import students_list, hello_world, request_
from teachers.views import run
from groupes.views import Groupe_


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('students-list/', students_list),
    path('teachers/', run),
    path('groupes/', Groupe_),
    path('students/', request_),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),


    ] + urlpatterns