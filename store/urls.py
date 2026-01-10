from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
     path('products/', views.products, name='products'),
    path('analytics/', views.analytics, name='analytics'),
     path('settings/', views.settings_page, name='settings'),

    path('login/', auth_views.LoginView.as_view( template_name='store/login.html' ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('signup/', views.signup, name='signup'),
    
    path('roadmap/python/', views.python_roadmap, name='python_roadmap'),
    path('roadmap/web/', views.web_roadmap, name='web_roadmap'),


    path('roadmap/java/', views.java_roadmap, name='java_roadmap'),
    path('roadmap/c/', views.c_roadmap, name='c_roadmap'),
    path('roadmap/cpp/', views.cpp_roadmap, name='cpp_roadmap'),
    path('roadmap/react/', views.react_roadmap, name='react_roadmap'),
    path('roadmap/sql/', views.sql_roadmap, name='sql_roadmap'),
    path('roadmap/r/', views.r_roadmap, name='r_roadmap'),

    path('learn/<int:course_id>/', views.course_learn, name='course_learn'),
    path('complete/<int:step_id>/', views.complete_step, name='complete_step'),



]
