from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

def unauthenticated_user(view_func):
	def wrapper_func(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect("student_home")
		else:
			return view_func(request,*args,**kwargs)

	return wrapper_func




def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request,*args,**kwargs):
			group = None
			if request.user.groups.exists():
				group=request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request,*args,**kwargs)
			else:
				return HttpResponse("Oops!You are not authorised to view this page....")
		return wrapper_func
	return decorator





def student_only(view_func):
	def wrapper_func(request,*args,**kwargs):
		group=None
		if request.user.groups.exists():
			group=request.user.groups.all()[0].name
		if group=="company":
			return HttpResponseRedirect(reverse("logout"))
		if group=="student":
			return view_func(request,*args,**kwargs)

	return wrapper_func
