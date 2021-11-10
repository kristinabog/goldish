from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_wishlist, name='wishlist'),
    path(
        'add_to_wishlist/<product_id>',
        views.add_to_wishlist,
        name='add_to_wishlist'),
]
