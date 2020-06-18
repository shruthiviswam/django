from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    gender=models.CharField(max_length=10,default='NA')

    class Meta:
        verbose_name_plural = 'student_details'

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=10)
    dept = models.CharField(max_length=20)
    joindate = models.DateField()
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Employee_details'

    def __str__(self):
        return self.name

class EmployeeData(models.Model):
    name = models.CharField(max_length=10)
    dept = models.CharField(max_length=20)
    upload_file=models.FileField(upload_to="documents")

    class Meta:
        verbose_name_plural = 'Employee Images'

    def __str__(self):
        return self.name


class Registration(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    country=models.CharField(max_length=50)
    address=models.TextField()
    password=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="Registration Details"

    def __str__(self):
        return self.username

class StudentAPI(models.Model):
    name=models.CharField(max_length=20)
    address=models.TextField()

    def __str__(self):
        return self.name