from django.db import models

# Create your models here.

class servertype(models.Model):
    serverType = models.CharField(max_length=30)

class center(models.Model):
    center = models.CharField(max_length=30)

class bladeinfo(models.Model):
    bladeId = models.CharField(max_length=30,primary_key=True)
    bladeNo   = models.IntegerField()
    bladeSerial = models.CharField(max_length=30)

class bladechassis(models.Model):
    bladeChassisId = models.CharField(max_length=30,primary_key=True)
    bladeChassisNo = models.IntegerField()
    bladeChassisSerial = models.CharField(max_length=30)

class serverinfo(models.Model):
    ipaddress = models.GenericIPAddressField()
    os = models.CharField(max_length=30)

class esxi(models.Model):
    #have to change the Musician becasue copied form other site
    inventoryID = models.CharField(max_length=30)
    esxiid = models.CharField(max_length=100, primary_key=True)
    ipaddress = models.GenericIPAddressField()
    bladechassisNo = models.IntegerField()
    bladeNo = models.IntegerField()
