from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import Product
from .models import Wishlist


@login_required
def get_wishlist(request):
    """
    Rendering the user's wishlist
    """
    wishlist = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)

    wishlist = Wishlist.objects.get(user=request.user)

    if wishlist:
        if product in wishlist:
        messages.error(request, "Item is already in your wishlist")
        else:
        wishlist.save(product)
        messages.success(
            request, f'Added {product.name} to your wishlist')
    else:



    template = 'wishlist/wishlist.html'
    context = {
        'product': product,
        'wishlist': wishlist,
    }

    return render(request, template, context)
