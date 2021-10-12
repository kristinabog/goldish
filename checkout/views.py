from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JjSKEIWZsxDrrObPyCRxJzMNUT9aEf2YylD1h7AcCi1NlJlBGSvWtVsf8o3wjt3Vqggp5h7YjPKbLXbyXbvFX7N001TcgrUwX',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
