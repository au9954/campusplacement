from django.urls import path

from . import views

urlpatterns=[

	
	path('signup/',views.signup_view,name="signup"),
	path('login',views.login_view,name="login"),
	path('logout/',views.logout_view,name="logout"),
	path('login/stu_home',views.student_home,name="student_home"),
	path('login/stu_home/companylist',views.company_list_view,name="company_list_view"),
	path('login/stu_home/companylist/<int:id>',views.company_detail_view,name="company_detail_view"),
	path('login/stu_home/<int:id>',views.student_profile,name="student_profile"),
	path('login/stu_home/<int:id>/update',views.update_view,name="student_update"),
	path('login/stu_home/change_password',views.change_password,name="change_password")
]