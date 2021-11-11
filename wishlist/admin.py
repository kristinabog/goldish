from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('__str__'),

admin.site.register(Wishlist, WishlistAdmin)
