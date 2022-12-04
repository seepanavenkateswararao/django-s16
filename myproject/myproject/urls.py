from django.contrib import admin
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('MyProjectSignup/MyProjectLogin/',views.loginpage),
    path('MyProjectSignup/',views.signuppage),
    path('MyProjectLogin/',views.loginpage),
    path('MyProjectLogin/MyProjectSignup/',views.loginpage),
    path('MyProjectLogin/settings.html',views.settings),
    path('MyProjectLogin/edit_details.html',views.edit_details),
    path('MyProjectLogin/loans.html',views.loan),
    path('MyProjectLogin/delete_account.html',views.delete_account),
    path('MyProjectLogin/eWallet',views.ewallet),
    path('MyProjectLogin/money_transfer.html',views.money_transfer),
    path('MyProjectLogin/online_payment.html',views.online_pay),
    path('MyProjectLogin/profile.html',views.indexs),
    path('faq.html', views.faq),
    path('payments.html',views.payments),
    path('nri.html', views.nri),
    path('deposits.html', views.deposits),
    path('fastag.html', views.fastag),
    path('About_us.html',views.aboutus),
    path('education_loan.html',views.edu_loan),
    path('MyProjectLogin/MyProjectHome.html',views.homepage),
    path('app_loan.html',views.app_loan),
    path('MyProjectLogin/money_transfer.html',views.app_loan),
    path('indexs.html', views.indexs),
    path('getquery',views.getquery,name='getquery'),
    path('sortdata',views.sortdata,name='sortdata')

]
