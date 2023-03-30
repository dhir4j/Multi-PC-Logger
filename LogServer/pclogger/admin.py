from django.contrib import admin
from .models import PC, PcInfo, PcInfoAdmin

admin.site.register(PC)
admin.site.register(PcInfo, PcInfoAdmin)
