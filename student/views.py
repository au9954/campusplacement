from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from company.models import Company
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import stu_register_form,stu_profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .decorators import unauthenticated_user,student_only,allowed_users
from django.core.paginator import Paginator

@unauthenticated_user
def signup_view(request):
    registered = False
    if request.method == 'POST':
        user_form = stu_register_form(data=request.POST)
        profile_form = stu_profile(data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            stu_group=Group.objects.get(name='student')
            user.groups.add(stu_group)
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = stu_register_form()
        profile_form = stu_profile()
    return render(request,'studentsignup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


@unauthenticated_user
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('student_home')
            else:
                return HttpResponse("Your account is inactive")
        else:
            print("Your are not a valid user")
            messages.error(request, "Invalid username or password.")
    else:
        return render(request,'studentlogin.html',{})




@login_required(login_url='student/login')
@allowed_users(allowed_roles=['student'])
#@student_only
def logout_view(request):
    logout(request)
    return render(request,"studentlogout.html")


@login_required(login_url='student/login/')
@allowed_users(allowed_roles=['student'])
#@student_only
def student_home(request):
    stu_list=request.user.id
    detail=Student.objects.filter(user=stu_list)
    return render(request,"studenthome.html",{"detail":detail})


@login_required(login_url='student/login')
@allowed_users(allowed_roles=['student'])
#@student_only
def student_profile(request,id):
    obj=get_object_or_404(Student,id=id)
    context={
    "object":obj
    }
    return render(request,"studentprofile.html",context)


@login_required(login_url='student/login')
@allowed_users(allowed_roles=['student'])
#@student_only
def update_view(request,id):
    obj=Student.objects.get(id=id)
    form=stu_profile(instance=obj)
    if request.method=="POST":
        form=stu_profile(data=request.POST,files=request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("student_home")
    context={"form":form}
    return render(request,"studentupdate.html",context)


@login_required(login_url='student/login')
@allowed_users(allowed_roles=['student'])
def company_list_view(request):
    queryset=Company.objects.all()
    stu=request.user.id
    detail=Student.objects.filter(user=stu)
    print(detail)
    branch=str(detail[0].branch)
    print(branch)
    if branch=="Information Technology":
        y=Company.objects.filter(information_technology="Yes")
    if branch=="Computer Science & Technology":
        y=Company.objects.filter(cse="Yes")
    if branch=="Mechanical Engineering":
        y=Company.objects.filter(mechanical="Yes")
    if branch=="Electronics & Communication":
        y=Company.objects.filter(ece="Yes")
    if branch=="Eletrical Engineering":
        y=Company.objects.filter(ee="Yes")
    if branch=="Civil Engineering":
        y=Company.objects.filter(civil="Yes")
    context={
    "object_list":y
    }
    return render(request,"companylist.html",context)


@login_required(login_url='student/login')
@allowed_users(allowed_roles=['student'])
#@student_only
def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Your password has been successfully updated")
            return redirect('student_home')
        else:messages.error(request,"Oops!There was some error.please try again.")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'change_password.html',{'form':form})


@login_required(login_url='student/login')
@allowed_users(allowed_roles=['student'])
def company_detail_view(request,id):
    obj=get_object_or_404(Company,id=id)
    stu=request.user.id
    detail=Student.objects.filter(user=stu)
    if(detail[0].class_10>=obj.min_10_percent and detail[0].class_12>=obj.min_12_percent
        and detail[0].btech_cgpa>=obj.min_btech_cgpa and detail[0].no_of_backlogs<=obj.no_of_backlogs):
        context={
        "object":obj
        }
        return render(request,"companydetail.html",context)
    else:
        context={
        'object':obj,
        'a':detail[0].class_10,
        'b':detail[0].class_12,
        'c':detail[0].btech_cgpa,
        'd':detail[0].no_of_backlogs

        }
        return render(request,"notallowed.html",context)



@login_required(login_url='student/login')
@allowed_users(allowed_roles=['student'])
def apply_view(request,id):

    return HttpResponse("Applied")
