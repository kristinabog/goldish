from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import Product
from .models import Wishlist


@login_required
def get_wishlist(request):
    """
    Rendering the user's wishlist
    """
    wishlist_products = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlist_products': wishlist_products,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)

    wishlist_items = Wishlist.objects.filter(product=product,
                                             user=request.user)

    if len(wishlist_items) == 1:
        messages.error(request, "Item is already in your wishlist")
    else:
        wishlist_item = Wishlist(product=product, user=request.user)
        wishlist_item.save()
        messages.success(
            request, f'Added {product.name} to your wishlist')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.filter(product=product, user=request.user)
    wishlist_item.delete()
    messages.success(
            request, f'Removed {product.name} from your wishlist')

    return redirect(reverse('wishlist'))
