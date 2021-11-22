from django.contrib import admin
from django.urls import path,include
from Blog import views

urlpatterns = [
    path('', views.home,name='home'),
    path('home/', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('about/', views.about,name='about'),
    path('serch_bar/', views.serch_bar,name='serch_bar'),
    path('show_data/<str:serch_catogery>/', views.show_data,name='show_data'),
    path('blog_page/<int:serch_value>/', views.blog_page,name='blog_page'),
    path('contact/', views.contact,name='contact')
   

]
