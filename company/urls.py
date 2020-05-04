from django.urls import path

from . import views




urlpatterns=[
	path('signup/',views.comp_signup_view,name="comp_signup_view"),
	path('login',views.comp_login_view,name="comp_login_view"),
	path('logout/',views.comp_logout_view,name="comp_logout_view"),
	path('login/comp_home',views.company_home,name="company_home"),
	path('login/comp_home/<int:id>',views.company_profile,name="company_profile"),
	path('login/comp_home/<int:id>/update',views.company_update,name="company_update"),
	path('login/comp_home/change_password',views.company_change_password,name="company_change_password")




]