
from django.contrib import admin
from django.urls import path ,include
from .views import About,Home,Savedata,ShowData
urlpatterns = [
    path('Home',Home,),
    path('',Home,name='Home'),
    path('About',About,name='About'),
    path('Savedata',Savedata,name='Savedata'),
    path('ShowData',ShowData,name='ShowData')
]