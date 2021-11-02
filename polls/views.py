from django.http import HttpResponse, Http404
from .models import Department, Employee
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
    employees = Employee.objects.all()
    required_emp = []
    for emp in employees:
        if emp.department.id == department_id:
            required_emp.append(emp.employee_name)
    return HttpResponse(output + str(required_emp))


def department_detail(request):
    department_list = Department.objects.all()
    template = loader.get_template('polls/departments.html')
    context = {
       'department_list' : department_list
    }
    return HttpResponse(template.render(context, request))


def register_employee(request):

    department_list = Department.objects.all()
    context = {
        'department_list': department_list
    }
    return render(request, 'polls/add_employee.html', context)


def registration_done(request):
    dep = Department.objects.get(pk=request.POST['department'])
    emp = Employee(department=dep,
                   employee_name='{} {}'.format(request.POST["fname"], request.POST["lname"]))
    emp.save()
    return HttpResponse(f'<b>Name</b>:{request.POST["fname"]} {request.POST["lname"]}<br><b>Department:</b> {dep.department_name}')
    # return render(request, 'polls/registration_done.html', {})
