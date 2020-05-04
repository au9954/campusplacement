from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import request
from .models import Company
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator,MaxLengthValidator


class comp_register_form(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(),max_length=25)
	email   =forms.EmailField(required=True,widget=forms.TextInput(attrs={"placeholder":"Company Email"}))
	class Meta():
		model  = User
		fields = ('username','password','email')


class comp_profile(forms.ModelForm):
	job_type=[('Full Time','Full Time'),('Intern','Internship'),('Others','Others'),]

	company_name = forms.CharField(max_length=100,required=True,
	widget=forms.TextInput(attrs={"placeholder":"Company Full Name"}))

	est_year = forms.CharField(label='Year Established',max_length=100,required=True,help_text="*required",
	widget=forms.TextInput(attrs={"placeholder":"Established year"}))

	hr_name = forms.CharField(max_length=100,help_text="*required",required=True,
	widget=forms.TextInput(attrs={"placeholder":"HR Name"}))

	hr_phn = forms.CharField(label='HR Phone',validators=[MaxLengthValidator(10),MinLengthValidator(10)],required=True,
	max_length=10,help_text="*required",widget=forms.TextInput(attrs={"placeholder":"HR Phone"}))

	headquarters=forms.CharField(required=True,help_text="*required")

	about=forms.CharField(max_length=2000,required=True,help_text='Please write in brief about job position and your company',
	widget=forms.Textarea(attrs={"placeholder":"About the Company"}))

	job_type=forms.ChoiceField(required=True,choices=job_type,help_text="Please Select the job type")

	designation=forms.CharField(required=True,help_text="*required",
	widget=forms.TextInput(attrs={"placeholder":"Job Designation"}))

	min_10_percent=forms.FloatField(required=True,validators=[MinValueValidator(0),MaxValueValidator(100)],
	help_text='Please enter 10th cutoff marks in %',
	widget=forms.TextInput(attrs={"placeholder":"In percentage"}),label='Cutoff Marks 10th')

	min_12_percent=forms.FloatField(required=True,validators=[MinValueValidator(0),MaxValueValidator(100)],
	help_text='Please enter 12th cutoff marks in %',
	widget=forms.TextInput(attrs={"placeholder":"In percentage"}),label='Cutoff Marks 12th')

	min_btech_cgpa=forms.FloatField(required=True,validators=[MinValueValidator(0),MaxValueValidator(100)],
	help_text='Please enter Btech cutoff cgpa',
	widget=forms.TextInput(attrs={"placeholder":"In CGPA"}),label='Cutoff Btech Cgpa')

	ctc=forms.FloatField(required=True,widget=forms.TextInput(attrs={"placeholder":"In LAKHS"}))

	bond_years=forms.FloatField(required=True,widget=forms.TextInput(attrs={"placeholder":"Bond Years"}))

	bond_amount=forms.FloatField(required=True,widget=forms.TextInput(attrs={"placeholder":"Bond Amount"}))
	
	no_of_backlogs=forms.FloatField(required=True,help_text="*required",
	widget=forms.TextInput(attrs={"placeholder":"Number of Backlogs allowed"}))


	class Meta():
		model=Company
		fields=('company_name','est_year','hr_name','hr_phn','headquarters','about','job_type',
			'designation','min_10_percent','min_12_percent','min_btech_cgpa',
			'information_technology','mechanical','cse','ee','ece','civil',
			'ctc','bond_years','bond_amount','no_of_backlogs')


