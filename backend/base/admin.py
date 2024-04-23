

# Register your models here.
from django.contrib import admin
from .models import UserProfile, CustomerProfile, SellerProfile, Service, PicsPosts, Appointment, NextAppointment

admin.site.register(UserProfile)
admin.site.register(CustomerProfile)
admin.site.register(SellerProfile)
admin.site.register(Service)
admin.site.register(PicsPosts)
admin.site.register(Appointment)
admin.site.register(NextAppointment)
