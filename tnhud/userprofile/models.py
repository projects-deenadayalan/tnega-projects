from django.db import models

# Create your models here.
class UserProfile(models.Model):
    owner_type=(('LL','Land Lords'),('PM','property Manager'),('TT','TENANT'))
    title=models.CharField(max_length=10)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_lenght=200)
    category=model.CharField(max_length=2,choices=owner_type,default='TT')
    address_line1=models.CharField(max_length=255)
    address_line2=models.CharField(max_length=255)
    address_line3=models.CharFiled(max_length=255)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    pin=models.CharField(max_length=30)
    mobile_number=DecimalField(max_digits=10)
    email=CharField(max_length=50)
    registered_on=DateTimeField(auto_now=true)
    updated_on=DateTimeField(auto_now=false)
