from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """
    Model with the list of wishlist items of the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wishlist_items = models.ManyToManyField(Product,
                                            related_name='wishlist_products')

    def __str__(self):
        return f'WishList - {self.user}'
