from django.db import models


class Customer(models.Model):
    tenure = models.FloatField()
    preferredlogindevice = models.CharField(max_length=20)
    citytier = models.FloatField()
    warehousetohome = models.FloatField()
    preferredpaymenthome = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    hourspendonapp = models.FloatField()
    numberofdeviceregistered = models.FloatField()
    preferedordercat = models.CharField(max_length=20)
    satisfactionscore = models.FloatField()
    maritalstatus = models.CharField(max_length=20)
    noofaaddress = models.FloatField()
    complain = models.FloatField()
    orderamounthikefromlastyear = models.FloatField()
    couponused = models.FloatField()
    ordercount = models.FloatField()
    daysincelastorder = models.FloatField()
    cashbackamount = models.FloatField()
    userid = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
