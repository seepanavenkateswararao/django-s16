from random import random
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
import random
from .models import *
from . import forms

from .models import User

def homepage(request):
    template=loader.get_template('MyProjectHome.html')
    return HttpResponse(template.render())
def loginpage(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=User.objects.get(uname=uname)
        if user:
            if user.pwd==pwd:
                return render(request, 'profile_base_layout.html')
            else:
                message="Invalid Password"
                return render(request, 'MyProjectLogin.html',{'msg':message})
        else:
            message = "Invalid Credentials"
            return render(request, 'MyProjectLogin.html', {'msg': message})
    return render(request, 'MyProjectLogin.html')
def signuppage(request):
    if request.method=="POST":
        fname=request.POST['fname']
        uname=request.POST['uname']
        emails=request.POST['emails']
        ano=request.POST['ano']
        pwd=request.POST['pwd']
        cpwd=request.POST['cpwd']
        gender=request.POST['gender']
        obj=User()
        obj.fname=fname
        obj.uname=uname
        obj.emails=emails
        obj.ano=ano
        obj.pwd=pwd
        obj.cpwd=cpwd
        obj.gender=gender

        user=User.objects.filter(uname=uname)
        if user:
            message="user already exist"
            return render(request,'MyProjectSignup.html',{'msg':message})
        else:
            if pwd==cpwd:
                obj.save()
                return redirect('MyProjectLogin/')
            else:
                message = "password and confirm password must be same"
                return render(request, 'MyProjectSignup.html', {'msg': message})

    return render(request,'MyProjectSignup.html')

def loan(request):
    return render(request, "loans.html")

def ewallet(request):
    return render(request, "eWallet.html")

def online_pay(request):
    return render(request, "online_payment.html")

def settings(request):
    return render(request, "settings.html")


def edit_details(request):
    if request.method == "POST":
        # POST actions for BasicDetailsForms
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form = forms.BasicDetailsForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.BasicDetailsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()

        # POST actions for PresentLocationForm
        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form = forms.PresentLocationForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.PresentLocationForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()

                # POST actions for Password change
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

        return redirect("profiles/edit_details.html")

    else:  # GET actions
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form1 = forms.BasicDetailsForm(instance=curr_user)  # basic details
        except:
            form1 = forms.BasicDetailsForm()

        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form2 = forms.PresentLocationForm(instance=curr_user)  # location
        except:
            form2 = forms.PresentLocationForm()

        # change password
        form3 = PasswordChangeForm(request.user)

        dici = {"form1": form1, "form2": form2, "form3": form3}
        return render(request, "edit_details.html", dici)


def delete_account(request):
    return render(request, "delete_account.html")


def randomGen():
    # return a 6 digit random number
    return int(random.uniform(100000, 999999))


def indexs(request):
    try:
        curr_user = Status.objects.get(user_name=request.user)  # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = Status()
        curr_user.account_number = randomGen()  # random account number for every new user
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "profile.html", {"curr_user": curr_user})

def faq(request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render())

def payments(request):
    template = loader.get_template('payments.html')
    return HttpResponse(template.render())

def nri(request):
    template = loader.get_template('nri.html')
    return HttpResponse(template.render())

def fastag(request):
    template = loader.get_template('fastag.html')
    return HttpResponse(template.render())
def deposits(request):
    template = loader.get_template('deposits.html')
    return HttpResponse(template.render())
def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()

            curr_user = models.MoneyTransfer.objects.get(enter_your_user_name=request.user)
            dest_user_acc_num = curr_user.enter_the_destination_account_number

            temp = curr_user  # NOTE: Delete this instance once money transfer is done

            dest_user = models.Status.objects.get(account_number=dest_user_acc_num)  # FIELD 1
            transfer_amount = curr_user.enter_the_amount_to_be_transferred_in_INR  # FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user)  # FIELD 3

            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount

            # Save the changes before redirecting
            curr_user.save()
            dest_user.save()

            temp.delete()  # NOTE: Now deleting the instance for future money transactions

        return redirect("profile.html")
    else:
        form = forms.MoneyTransferForm()
    return render(request, "money_transfer.html", {"form": form})

def aboutus(request):
    template = loader.get_template('About_us.html')
    return HttpResponse(template.render())

def edu_loan(request):
    template = loader.get_template('education_loan.html')
    return HttpResponse(template.render())

def app_loan(request):
    template = loader.get_template('app_loan.html')
    return HttpResponse(template.render())

arr = ['saving','current','Business']
globalcnt = dict()

def indexs(request):
    mydictionary = {
        "arr" : arr
    }
    return render(request,'indexs.html',context=mydictionary)

def getquery(request):
    q = request.GET['languages']
    if q in globalcnt:
        # if already exist then increment the value
        globalcnt[q]=globalcnt[q]+1
    else:
        # first occurrence
        globalcnt[q]=1
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'indexs.html',context=mydictionary)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'indexs.html',context=mydictionary)




