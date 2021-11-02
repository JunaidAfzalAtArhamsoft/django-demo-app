from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    department_location = models.CharField(max_length=150)

    def __str__(self):
        return '{} in {}'.format(self.department_name, self.department_location)


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=60)

    def __str__(self):
        return self.employee_name
