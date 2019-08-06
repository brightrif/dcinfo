from django.contrib import admin

# Register your models here.
from . models import dataCenterModel,vendorModel,rackModel,deviceModel,serverModel,serverVirtualModel,networkModel
# Registered modules
admin.site.register(dataCenterModel)
admin.site.register(vendorModel)
admin.site.register(rackModel)
admin.site.register(deviceModel)
admin.site.register(serverModel)
admin.site.register(serverVirtualModel)
admin.site.register(networkModel)
