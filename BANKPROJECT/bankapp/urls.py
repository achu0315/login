from . import views
from django.urls import path

app_name='bankApp'

urlpatterns = [
   
    path('',views.demo,name="demo"),
    path('register/',views.register,name='registerdata'),
    path('login/',views.loginuser,name='logindata'),

    path('logout/',views.logout,name='logout'),
    path('form/',views.form,name='form'),
    path('success/',views.success,name='success'),




]
