from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Employee,Registration,EmployeeData,StudentAPI
from .forms import StudentForm, EmployeeForm, StudentDataForm,signupForm,EmployeeForm1,EmployeeForm2,MailSendingForm
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.shortcuts import redirect
from rest_framework import generics
from . import serializers



# Create your views here.
def home(request):
    head = "Fruits"
    a = "Apple"
    b = "Mango"
    c = "Orange"
    d = "Strawberry"
    s = "These are some of the fruits."
    return render(request, 'newapp/home.html', {'head': head, 'a': a, 'b': b, 'c': c, 'd': d, 's': s})


def template(request):
    list1 = [2, 4, 6, 8, 10]

    num = 100
    return render(request, 'newapp/templateTags.html', {'list1': list1, 'dict1': dict1, 'text': text, 'num': num})


def layout(request):
    return render(request, 'newapp/layout.html')


def apple(request):
    return render(request, 'newapp/apple.html')


def mango(request):
    return render(request, 'newapp/mango.html')


def student1(request):
    students = Student.objects.all()
    return render(request, 'newapp/student.html', {'students': students})


def emp1(request):
    emp = Employee.objects.all()
    return render(request, 'newapp/employee.html', {'emp': emp})


def studentDataLink(request):
    students = Student.objects.all()
    return render(request, 'newapp/studentdata.html', {'students': students})


def studentDetails(request, id):
    students = Student.objects.get(id=id)
    return render(request, 'newapp/studentdetails.html', {'students': students})


def empdata(request):
    emp = Employee.objects.all()
    return render(request, 'newapp/empdata.html', {'emp': emp})


def empdisp(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'newapp/empdisp.html', {'emp': emp})


# def crudeoperations(request):
# student1=Student(name='Aima',age=25,address='kerala')
# student1.save()
# return HttpResponse('Saved to the database!')

# student2 = Student()
# student2.name = 'Reeba'
# student2.age = 34
# student2.address = 'Kerala'
# student2.save()
# return HttpResponse('Saved to the database!')

# student3 = Student.objects.create(name='Zahrah', age=22, address='UK')
# return HttpResponse('Saved to the database!')

# student4 = Student.objects.get(id=5)
# student4.name = 'Remya'
# student4.age = 55
# student4.save()
# return HttpResponse('Updated to the Database!')

# student5 = Student.objects.get(id=5)
# student5.delete()
# return HttpResponse('Deleted!')

# emp2 = Employee.objects.get(id='2')
# emp2.name = 'Alina'
# emp2.dept = 'Business Management'
# emp2.save()
# return HttpResponse('Updated!')
#
# emp3 = Employee.objects.get(id='1')
# emp3.delete()
# return HttpResponse('Deleted!')


def modelform(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data is saved to the Database!')
        # else:
        #     return HttpResponse(forms.errors)
    return render(request, 'newapp/modelform.html', {'form': form})

def emplform(request):
    form = EmployeeForm2()
    if request.method == 'POST':
        form = EmployeeForm2(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Data is saved to the Database!')
        # else:
        #     return HttpResponse(forms.errors)
    return render(request, 'newapp/emp.html', {'form': form})


def empform(request):
    f = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data is saved to the Database!')
        # else:
        #     return HttpResponse(forms.errors)
    return render(request, 'newapp/empform.html', {'f': f})


def studentformdata(request):
    form = StudentDataForm()
    if request.method == 'POST':
        form=StudentDataForm(request.POST)
        if form.is_valid:
    
            name = request.POST.get('name')
            age = request.POST.get('age')
            address = request.POST.get('address')
            gender = request.POST.get('gender')

            s = Student()
            s.name = name
            s.age = age
            s.address = address
            s.gender=gender
            s.save()
            return HttpResponse('Data Saved!')
    return render(request, 'newapp/studentform.html', {'form': form})


def signup(request):
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid:
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            username=request.POST.get('username')
            gender=request.POST.get('gender')
            address=request.POST.get('address')
            country=request.POST.get('country')
            password=request.POST.get('password')
            confirmPassword=request.POST.get('confirmPassword')
            date_of_birth=request.POST.get('date_of_birth')

            r=Registration()

            r.firstname=firstname
            r.lastname=lastname
            r.username=username
            r.gender=gender
            r.address=address
            r.country=country
            r.password=password
            r.confirmPassword=confirmPassword
            r.date_of_birth=date_of_birth

            r.save()

            return HttpResponse('Form Submitted Successfully!')

    return render(request,'newapp/signup.html',{'form':form})

def Employee1(request):
    
    if request.method=='POST':
        form=EmployeeForm1(request.POST,request.FILES)
        if form.is_valid():
            name = request.POST.get('name')
            dept = request.POST.get('dept')
            upload_file=request.POST.get('upload_file')

            emp=EmployeeData()

            emp.name=name
            emp.dept=dept

            emp.upload_file=upload_file

            emp.save()
            
            return HttpResponse('Data is saved!')
    else:
        form=EmployeeForm1()

    return render(request,'newapp/emp.html',{'form':form})

def employeedetails(request):
    employees=EmployeeData.objects.all()
    return render(request,'newapp/employeedetails.html',{'employees':employees})

def emailconsole(request):
    send_mail('subject','Hello World','abc@gmail.com',['to_mail'],fail_silently=False)
    return HttpResponse('Mail Sent Successfully!')

def MailSending(request):
    form=MailSendingForm
    if request.method=='POST':
        form=MailSendingForm(request.POST,request.FILES)
        if form.is_valid:
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            from_mail=request.POST.get('from_mail')
            to_mail=request.POST.get('to_mail')
            attachment=request.POST.get('attachment')
            
            email=EmailMessage(subject,message,from_mail,[to_mail])

            email.attach(attachment.name,attachment.read(),attachment.content_type)

            email.send()

            return HttpResponse('Mail Sent Successfully!')
    
    else:
        form=MailSendingForm()

    return render(request,'newapp/mailsend.html',{'form':form})

def setSession(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['sessionusername']=username
        request.session['sessionpassword']=password
        return redirect('showSession')

    return render(request,'newapp/setsession.html')

def showSession(request):
    user=request.session['sessionusername']
    pwd=request.session['sessionpassword']

    return render(request,'newapp/showsession.html',{'user':user,'pwd':pwd})

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        userdata=Registration.objects.filter(username=username,password=password)
        if userdata:
            form=signupForm()
            request.session['username']=username
            user=request.session['username']
            # request.session.set.expiry(300)
            return render(request,'newapp/welcome.html',{'form':form,'user':user})
    
    return render(request,'newapp/register.html')

class ListStudent(generics.ListCreateAPIView):
    queryset= StudentAPI.objects.all()
    serializer_class=serializers.StudentSerializers

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset=StudentAPI.objects.all()
    serializer_class=serializers.StudentSerializers