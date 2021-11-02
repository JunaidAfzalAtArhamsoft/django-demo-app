from django.http import HttpResponse, Http404
from .models import Department
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import render
# Create your views here.


def hello_world(request):
    return HttpResponse('<h1>Hello World.<br>My first django app view.</h1>')


# def get_department(request, department_id):
#     try:
#
#         dep = Department.objects.get(pk=department_id)
#         dep = get_object_or_404(Department, pk=department_id)
#         output = '<h2>Details of department:</h2>' + f'<h3>Department Name:</h3><b>{dep.department_name}<b><br>' + \
#                  f'<h3>Department Location:</h3><b>{dep.department_location}<b><br>'
#         return HttpResponse(output)
#     except Department.DoesNotExist:
#         raise Http404('Department does not exist')


def get_department(request, department_id):

    # Other way to get department and raise error 404 if not exist
    dep = get_object_or_404(Department, pk=department_id)
    output = '<h2>Details of department:</h2>' + f'<h3>Department Name:</h3><b>{dep.department_name}<b><br>' + \
             f'<h3>Department Location:</h3><b>{dep.department_location}<b><br>'
    return HttpResponse(output)


def department_detail(request):
    department_list = Department.objects.all()
    template = loader.get_template('polls/departments.html')
    context = {
       'department_list' : department_list
    }
    return HttpResponse(template.render(context, request))


def register_employee(request):

    # template = loader.get_template('polls/add_employee.html')
    return render(request, 'polls/add_employee.html', {})


def registration_done(request):
    return render(request, 'polls/registration_done.html', {})
