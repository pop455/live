from . import views
from django.urls import path
urlpatterns = [

    path('',views.demo1,name='demo'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),

    ]