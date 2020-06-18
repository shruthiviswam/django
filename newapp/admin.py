from django.contrib import admin
from .models import Student
from .models import Employee
from .models import Registration
from .models import EmployeeData
from .models import StudentAPI

# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Registration)
admin.site.register(EmployeeData)
admin.site.register(StudentAPI)