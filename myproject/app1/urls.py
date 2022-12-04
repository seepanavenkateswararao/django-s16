from django.contrib import admin
from django.urls import path,include
from views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('MyProjectSignup/MyProjectLogin/',views.loginpage),
    path('MyProjectSignup/',views.signuppage),
    path('MyProjectLogin/',views.loginpage),
    path('MyProjectLogin/MyProjectSignup/',views.loginpage),
    path('MyProjectHome/',views.homepage),

]