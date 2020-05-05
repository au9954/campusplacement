from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):

	done=[('Yes','Yes'),('No','No')]

	job_type=[('Full Time','Full Time'),('Intern','Internship'),('Others','Others'),]

	user          = models.OneToOneField(User,on_delete=models.CASCADE)
	company_name  = models.CharField(max_length=30, blank=False, help_text='*Please type full name of your company')
	est_year      = models.CharField(max_length=4, blank=False, help_text="*optional")
	hr_name       = models.CharField(max_length=30, blank=False, help_text='*required')
	hr_phn        = models.CharField(max_length=10,validators=[MinLengthValidator(10),MaxLengthValidator(10)], blank=False, help_text='*required')
	headquarters  = models.CharField(max_length=30,blank=False, help_text='*optional')
	about         = models.TextField(max_length=1000, blank=False, help_text='*optional')
	job_type      = models.CharField(max_length=100, blank=False,choices=job_type)
	designation   = models.CharField(max_length=100, blank=False, help_text='*required')
	min_10_percent= models.FloatField(help_text='*In percent',validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False)
	min_12_percent= models.FloatField(help_text='*In percent',validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False)
	min_btech_cgpa= models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False)
	information_technology= models.CharField(blank=False, choices=done, max_length=10)
	mechanical= models.CharField(blank=False, choices=done, max_length=10)
	cse= models.CharField(blank=False, choices=done, max_length=10)
	ee= models.CharField(blank=False, choices=done, max_length=10)
	ece= models.CharField(blank=False, choices=done, max_length=10)
	civil= models.CharField(blank=False, choices=done, max_length=10)
	ctc           = models.FloatField( blank=False, help_text='In Lakhs')
	bond_years    = models.FloatField( blank=False, help_text='*required')
	bond_amount   = models.FloatField(help_text='*In Lakhs',blank=False)
	no_of_backlogs=models.IntegerField(blank=False,default=0)
	last_date_to_apply=models.DateField(blank=True,null=True)
#	email         = models.EmailField(max_length=254,blank=False, help_text='*required')
	

	def __str__(self):
		return self.company_name