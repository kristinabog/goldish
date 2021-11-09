from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Wishlist


@login_required
def get_wishlist(request):
    """
    Rendering the user's wishlist
    """
    wishlist = Wishlist.objects.filter(user=request.user)

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)
