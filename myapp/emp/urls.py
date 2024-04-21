from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import include
urlpatterns = [
    path("home/",emp_home),
    path('add-emp/',add_emp),
    path("modify-emp/",modify_emp),
    path("list-emp/",emp_list),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path("testimonials/",testimonials)
]
