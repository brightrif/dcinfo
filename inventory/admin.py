from django.contrib import admin

# Register your models here.
from . models import servertype,center, bladeinfo, bladechassis, serverinfo, esxi


admin.site.register(servertype)
admin.site.register(center)
admin.site.register(bladeinfo)
admin.site.register(bladechassis)
admin.site.register(esxi)
