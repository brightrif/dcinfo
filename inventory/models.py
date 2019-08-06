from django.db import models
# Create your models here.

class dataCenterModel(models.Model):
    datacenterId = models.AutoField(primary_key=True)
    datacenterName = models.CharField(max_length=30)
    datacenterCode = models.CharField(max_length=30)
    note = models.CharField(max_length=30)
    creationDate = models.DateField(auto_now_add = True)

class vendorModel(models.Model):
    vendorID = models.AutoField(primary_key=True)
    vendorName = models.CharField(max_length=30)
    contactNumber = models.CharField(max_length=30)
    note = models.CharField(max_length=30)
    date = models.DateField(auto_now_add = True)

class rackModel(models.Model):
    rackId = models.AutoField(primary_key=True)
    datacenterId = models.ForeignKey(dataCenterModel, on_delete=models.CASCADE)
    rackNo = models.IntegerField()
    rackLocation = models.CharField(max_length=30)
    rackName = models.CharField(max_length=30)
    note = models.CharField(max_length=30)
    date = models.DateField(auto_now_add = True)
    #rackPicture = models.CharField(max_length=30)

class deviceModel(models.Model):
    deviceId = models.AutoField(primary_key=True)
    deviceSn = models.CharField(max_length=30)
    vendor = models.ForeignKey(vendorModel, on_delete=models.CASCADE)
    rackId = models.ForeignKey(rackModel, on_delete=models.CASCADE)
    unitUStart = models.IntegerField()
    unitUEnd = models.IntegerField()
    deviceType = models.CharField(max_length=30)
    modelNumber = models.CharField(max_length=30)
    productId = models.CharField(max_length=30)
    warrentyStatus = models.CharField(max_length=30)
    warrentyExpireyDate = models.DateField(auto_now_add = True)
    note = models.CharField(max_length=30)
    date = models.DateField(auto_now_add = True)

class serverModel(models.Model):
    serverId = models.AutoField(primary_key=True)
    device = models.ForeignKey(deviceModel, on_delete=models.CASCADE)
    ServerIP = models.GenericIPAddressField()
    Servername = models.CharField(max_length=30)
    isPhysical = models.CharField(max_length=30)
    osFamily = models.CharField(max_length=30)
    os = models.CharField(max_length=30)
    hostName = models.CharField(max_length=30)
    memory = models.IntegerField()
    cpu = models.IntegerField()
    role = models.CharField(max_length=30)
    environamnt = models.CharField(max_length=30)
    note = models.CharField(max_length=30)
    date = models.DateField(auto_now_add = True)


class serverVirtualModel(models.Model):
    vServerId = models.AutoField(primary_key=True)
    device = models.ForeignKey(deviceModel, on_delete=models.CASCADE)
    ServerIP = models.GenericIPAddressField()
    serverName = models.CharField(max_length=30)
    osFamily = models.CharField(max_length=30)
    os = models.CharField(max_length=30)
    hostname = models.CharField(max_length=30)
    memory = models.IntegerField()
    cpu = models.IntegerField()
    Disk = models.IntegerField()
    datastores = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    environamnt = models.CharField(max_length=30)
    note = models.CharField(max_length=30)
    date = models.DateField(auto_now_add = True)


class networkModel(models.Model):
    networkId = models.AutoField(primary_key=True)
    ipaddress = models.GenericIPAddressField()
    device = models.ForeignKey(deviceModel, on_delete=models.CASCADE)
    note = models.CharField(max_length=30)
    date = models.DateField(auto_now_add = True)
