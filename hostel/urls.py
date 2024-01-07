from django.urls import path

from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('form',views.form , name='form'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('application_submit/', views.application_submit, name='application_submit'),
    path('accept_applications/',views.accept_applications, name='accept_applications'),    
    path('admin_login/',views.admin_login, name='admin_login' ),
    path('expire_allotement/', views.expire_allottment, name='expire_allotement')
]