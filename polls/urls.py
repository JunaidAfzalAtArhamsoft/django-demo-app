from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', views.hello_world, name='index'),
    path('departments/<int:department_id>', views.get_department, name='department_detail'),
    path('departments-detail', views.department_detail, name='departments_detail'),
    path('register', views.register_employee, name='employee_registration'),
    path('registration-done', views.registration_done, name='registration_done'),
]
