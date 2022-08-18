from django.contrib import admin
from django.urls import path


from django.urls import re_path as url


from django.conf.urls import include

'''
---------------- NOT UNDERSTAND------------------------
'''
urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^',include('EmployeeApi.urls'))
]
