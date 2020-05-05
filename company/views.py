from django.shortcuts import render,redirect,get_object_or_404
from .models import Company
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import comp_register_form,comp_profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .decorators import unauthenticated_user,allowed_users
from student.models import Student
from django.core.mail import send_mail

@unauthenticated_user
def comp_signup_view(request):
    registered = False
    if request.method == 'POST':
        user_form = comp_register_form(data=request.POST)
        profile_form = comp_profile(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            comp_group=Group.objects.get(name='company')
            user.groups.add(comp_group)
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = comp_register_form()
        profile_form = comp_profile()
    return render(request,'companysignup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



@unauthenticated_user
def comp_login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('company_home'))
            else:
                return HttpResponse("Your account is inactive")
        else:
            print("Your are not a valid user")
            messages.error(request, "Invalid username or password.")
    else:
        return render(request,'companylogin.html',{})


@login_required(login_url='company/login')
@allowed_users(allowed_roles=['company'])
def company_home(request):
    comp_list=request.user.id
    detail=Company.objects.filter(user=comp_list)
    context={"detail":detail}
    return render(request,"companyhome.html",context)


@login_required(login_url='company/login')
@allowed_users(allowed_roles=['company'])
def comp_logout_view(request):
    logout(request)
    return render(request,"companylogout.html")

@login_required(login_url='company/login')
@allowed_users(allowed_roles=['company'])
def company_profile(request,id):
    obj=get_object_or_404(Company,id=id)
    context={
    "object":obj
    }
    return render(request,"companyprofile.html",context)

@login_required(login_url='company/login')
@allowed_users(allowed_roles=['company'])
def company_update(request,id):
    obj=Company.objects.get(id=id)
    form=comp_profile(instance=obj)
    if request.method=="POST":
        form=comp_profile(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("company_home")
    context={"form":form}
    return render(request,"studentupdate.html",context)

@login_required(login_url='company/login')
@allowed_users(allowed_roles=['company'])
def company_change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Your password has been successfully updated")
            return redirect('company_home')
        else:messages.error(request,"Oops!There was some error.please try again.")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'changepassword.html',{'form':form})


@login_required(login_url='company/login')
@allowed_users(allowed_roles=['company'])
def student_list(request):
    comp=request.user.id
    comp_detail=Company.objects.filter(user=comp)
    comp_id=comp_detail[0].id
    queryset=Company.objects.get(id=comp_id).student_set.all().order_by('branch')
    print(queryset)
    context={
    "object_list":queryset
    }
    return render(request,"studentlist.html",context)


@login_required(login_url='company/login')
@allowed_users(allowed_roles=['company'])
def student_detail(request,id):
    obj=get_object_or_404(Student,id=id)
    u=obj.user.email
    context={
    "object":obj,"email":u
    }
    return render(request,"studentdetail.html",context)


@login_required(login_url='company/login')
@allowed_users(allowed_roles=['company'])
def select_view(request,id):
    obj=get_object_or_404(Student,id=id)
    receiver=obj.user.email
    sender=request.user.email
    compname=request.user.id
    detail=Company.objects.filter(user=compname)
    name=detail[0].company_name
    send_mail(
        'Selection Confirmation from ' + name,
        'Congratulations!You have been selected for interview.The interview details will be conveyed to your placement officer.All the best!',
        sender,[receiver],
        fail_silently=False,)
    return render(request,"selectionmail.html")



