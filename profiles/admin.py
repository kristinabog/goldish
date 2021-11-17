from django.contrib import admin
from .models import UserProfile, DeliveryAddress


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__'),


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('__str__'),


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(DeliveryAddress, DeliveryAddressAdmin)
