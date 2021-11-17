from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model for the categories of the products
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    """
    Model for the store products
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Model for reviews for an individual product
    """
    class Meta:
        """
        Descending the review dates
        """
        ordering = ['-date']

    product = models.ForeignKey(Product, null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
    username = models.ForeignKey(User, null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.date
