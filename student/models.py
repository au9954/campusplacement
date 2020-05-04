from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator
from django.contrib.auth.models import User
from django.urls import reverse
from company.models import Company
# Create your models here.


class Student(models.Model):
    branch=[('Information Technology','Information Technology'),
    ('Computer Science & Engineering','Computer Science & Engineering'),
    ('Electronics & Communication','Electronics & Communication'),
    ('Eletrical Engineering','Eletrical Engineering'),
    ('Mechanical Engineering','Mechanical Engineering'),
    ('Civil Engineering','Civil Engineering'),]
    gender=[('Female','Female'),('Male','Male'),('Other','Other')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True,help_text="Enter Full Name")
    gender=models.CharField(max_length=50,blank=False,choices=gender)
#    email = models.EmailField(max_length=150)
    phone_number=models.CharField(validators=[MaxLengthValidator(10),MinLengthValidator(10)],blank=False,max_length=10,help_text='*Enter 10 digit mobile number')
    roll_no=models.CharField(max_length=20,validators=[MaxLengthValidator(20),MinLengthValidator(8)],blank=False,help_text='*Enter University Roll No.')
    branch=models.CharField(max_length=100,blank=False,choices=branch,help_text="Select the Department")
#    language=models.CharField(max_length=100,blank=False,choices=language,help_text="Select the language you know best")
    dob   =models.DateField(blank=False,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    class_10=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False,help_text='Please enter 10th marks in %')
    class_12=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False,help_text='Please enter 10th marks in %')
    btech_cgpa=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False)
    no_of_backlogs=models.IntegerField(default=0,blank=False)
    father_name=models.CharField(max_length=50,blank=False)
    mother_name=models.CharField(max_length=50,blank=False)
    address=models.TextField(max_length=254,blank=False,help_text='Please enter your permanent address')
    photo=models.ImageField(upload_to="student_images/%Y/%m/%d/",default="default.jpg",blank=True,help_text='Please upload your recent photograph')
    placed=models.BooleanField(default=False)
    placed_in=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name



