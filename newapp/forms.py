from django import forms

from .models import Student, Employee,Registration,EmployeeData


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'dept', 'joindate', 'email']

class EmployeeForm1(forms.Form):
    name = forms.CharField(required=True)
    dept = forms.CharField()
    upload_file=forms.FileField()

class EmployeeForm2(forms.ModelForm):
    class Meta:
        model=EmployeeData
        fields = ['name','dept','upload_file']


class StudentDataForm(forms.Form):
    name = forms.CharField(required=True)
    age = forms.CharField(widget=forms.NumberInput)
    address = forms.CharField(widget=forms.Textarea)
    list1=[('M','Male'),('F','Female')]
    gender=forms.ChoiceField(choices=list1,widget=forms.RadioSelect)
    def clean_name(self):
        name = self.cleaned_data['name']
        if value.isupper():
            raise forms.ValidationError('please dont use uppercase')
        return name
    
class signupForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    username=forms.CharField(widget=forms.TextInput())

    GENDER_CHOICES=(
        ('male','male'),
        ('female','female')
    )
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
    date_of_birth=forms.DateField()
    country_choice=[
        ('India','India'),
        ('Pakistan','Pakistan'),
        ('China','China')
    ]
    country=forms.CharField(widget=forms.Select(choices=country_choice))
    address=forms.CharField(widget=forms.Textarea())
    password=forms.CharField(widget=forms.PasswordInput())
    confirmPassword=forms.CharField(widget=forms.PasswordInput())
    terms=forms.BooleanField()
    
    def clean_firstname(self):
        firstname=self.cleaned_data['firstname']
        if firstname.isupper():
            raise forms.ValidationError['Please use lowercase!']
        return firstname

    def clean_lastname(self):
        lastname=self.cleaned_data['lastname']
        if lastname.isupper():
            raise forms.ValidationError['Please use lowercase!']
        return lastname

    def clean_confirmPassword(self):
        password=self.cleaned_data['password']
        confirmPassword=self.cleaned_data['confirmPassword']
        if not password==confirmPassword:
            raise forms.ValidationError['Passwords not matching!']
        return password

class MailSendingForm(forms.Form):
    subject=forms.CharField()
    message=forms.CharField()
    from_mail=forms.CharField()
    to_mail=forms.CharField()
    attachment=forms.FileField()
    