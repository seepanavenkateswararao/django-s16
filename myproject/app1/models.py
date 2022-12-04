from django.db import models

class User(models.Model):
    fname=models.CharField(max_length=20,default='',null=False)
    uname=models.CharField(max_length=20,default='',null=False)
    emails=models.EmailField(max_length=20,default='',null=False)
    ano=models.IntegerField(max_length=20,default='',null=False)
    pwd=models.CharField(max_length=20,default='',null=False)
    cpwd = models.CharField(max_length=20, default='', null=False)
    gender=models.CharField(max_length=1,default='',null=False)

class BasicDetails (models.Model):
    # (Name, Sex, DOB, Annual income, Email, Mobile number, Occupation)
    name = models.CharField(max_length = 50, default = None)
    sex = models.CharField(max_length = 1, default = None)
    annual_income = models.IntegerField(default = 0)
    email = models.EmailField(default = None)
    mobile = models.IntegerField(default = 0)
    occupation = models.CharField(max_length = 50, default = None)
    DOB = models.DateField(default = None)
    user_name = models.CharField(max_length = 150, default = None)

class PresentLocation (models.Model):
    # (Country, State, City, Street, Pincode)
    country = models.CharField(max_length = 50, default = "India")
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    street = models.CharField(max_length = 50)
    pincode = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

class Status (models.Model):
    account_number = models.IntegerField()
    balance = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

class MoneyTransfer(models.Model):
    enter_your_user_name = models.CharField(max_length = 150, default = None)
    enter_the_destination_account_number = models.IntegerField()
    enter_the_amount_to_be_transferred_in_INR = models.IntegerField()

