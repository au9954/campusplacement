from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import request
from .models import Student
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator,MaxLengthValidator

class stu_register_form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(),max_length=25)
    email   =forms.EmailField(required=True,widget=forms.TextInput(attrs={"placeholder":"Your Email"}))
    class Meta:
        model=User
        fields=('username','password','email')



year=['1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008',
       '2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021',
       '2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033',
       '2034','2035','2036','2037','2038','2039','2040','2041','2042','2043','2044','2045',
       '2046','2047','2048','2049','2050']







class stu_profile(forms.ModelForm):
    branch=[('Information Technology','Information Technology'),
    ('Computer Science & Engineering','Computer Science & Engineering'),
    ('Electronics & Communication','Electronics & Communication'),
    ('Eletrical Engineering','Eletrical Engineering'),
    ('Mechanical Engineering','Mechanical Engineering'),
    ('Civil Engineering','Civil Engineering'),]
    gender=[('Female','Female'),('Male','Male'),('Other','Other')]
    

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder":"Your Full Name"}))
    gender=forms.ChoiceField(required=True,choices=gender)
    phone_number=forms.CharField(validators=[MaxLengthValidator(10),MinLengthValidator(10)],required=True,max_length=10,help_text='*Enter 10 digit mobile number',widget=forms.TextInput(attrs={"placeholder":"Enter 10 digit mobile number"}))
    roll_no=forms.CharField(max_length=20,validators=[MaxLengthValidator(20),MinLengthValidator(8)],required=True,help_text='*Enter University Roll No.',widget=forms.TextInput(attrs={"placeholder":"Enter University Roll"}))
    branch=forms.ChoiceField(required=True,choices=branch,help_text="Select the Department")
#    language=forms.ChoiceField(required=True,choices=language,help_text="Select the language you know best")
    dob   =forms.DateField(label='Date of Birth',widget=forms.SelectDateWidget(years=year),required=True)
    class_10=forms.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],required=True,help_text='Please enter 10th marks in %',widget=forms.TextInput(attrs={"placeholder":"In percentage"}))
    class_12=forms.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],required=True,help_text='Please enter 12th marks in %',widget=forms.TextInput(attrs={"placeholder":"In percentage"}))
    btech_cgpa=forms.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],required=True,widget=forms.TextInput(attrs={"placeholder":"Average CGPA yet"}))
    no_of_backlogs=forms.IntegerField(label='No. of active backlogs',required=True)
    father_name=forms.CharField(max_length=50,required=True,label='Father\'s Name',widget=forms.TextInput(attrs={"placeholder":"Father\'s Name"}))
    mother_name=forms.CharField(max_length=50,required=True,label='Mother\'s Name',widget=forms.TextInput(attrs={"placeholder":"Mother\'s' Name"}))
    address=forms.CharField(max_length=500,required=True,help_text='Please enter your permanent address',widget=forms.Textarea(attrs={"placeholder":"Permanent Address"}))
    photo=forms.ImageField(required=False,help_text="Please upload your recent photograph")

    class Meta:
        model  = Student
        fields = ('name','gender','phone_number','roll_no','branch','dob',
            'class_10','class_12','btech_cgpa','no_of_backlogs','father_name',
            'mother_name','address','photo')
