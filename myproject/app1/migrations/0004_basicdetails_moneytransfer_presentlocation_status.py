# Generated by Django 4.1.2 on 2022-11-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_user_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('sex', models.CharField(default=None, max_length=1)),
                ('annual_income', models.IntegerField(default=0)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('mobile', models.IntegerField(default=0)),
                ('occupation', models.CharField(default=None, max_length=50)),
                ('DOB', models.DateField(default=None)),
                ('user_name', models.CharField(default=None, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_your_user_name', models.CharField(default=None, max_length=150)),
                ('enter_the_destination_account_number', models.IntegerField()),
                ('enter_the_amount_to_be_transferred_in_INR', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PresentLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='India', max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('user_name', models.CharField(default=None, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('user_name', models.CharField(default=None, max_length=150)),
            ],
        ),
    ]
