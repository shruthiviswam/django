from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.home),
    path('template', views.template),
    path('layout', views.layout),
    path('apple', views.apple),
    path('mango', views.mango),
    path('student-info', views.student1),
    path('employee', views.emp1),
    path('studentlink', views.studentDataLink),
    path('studentDetails/<id>', views.studentDetails),
    path('emp', views.empdata),
    path('empdisp/<id>', views.empdisp),
    # path('crud', views.crudeoperations),
    path('modelform', views.modelform),
    path('empform', views.empform),
    path('form', views.studentformdata),
    path('form2',views.signup),
    path('empimg',views.Employee1),
    path('img',views.emplform),
    path('employeedetails',views.employeedetails),
    path('emailconsole',views.emailconsole),
    path('mailsending',views.MailSending),
    path('setSession',views.setSession,name='setSession'),
    path('showSession',views.showSession,name='showSession'),
    path('login',views.login),
    path('api',views.ListStudent.as_view()),
    path('<int:pk>',views.DetailStudent.as_view())
]
