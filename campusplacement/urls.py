"""campusplacement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import  include,path
from pages.views import home_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
#    path('about/',about_view,name="about"),
#    path('contact/',contact_view,name="contact"),
    path('company/',include('company.urls')),
    path('student/',include('student.urls')),
#    path('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_password_reset',),
#    path('admin/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done',),
#    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm',),
#    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete',),
    path('login/password-reset/',
        auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"),name="password_reset"),
    path('login/password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_done.html"),name="password_reset_done"),
    path('login/password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_confirm.html"),name="password_reset_confirm"),
    path('login/password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_complete.html"),name="password_reset_complete"),

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)