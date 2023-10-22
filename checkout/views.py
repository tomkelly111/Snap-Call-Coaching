from django.shortcuts import render, redirect, reverse
# from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    # if not bag:
    #     messages.error(request, "There's nothing in your bag at the moment")
    #     return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O3xb4DDE8VL8FuCABT3lC3HllNvTlPB2AvF7VBs6Q49OaxRl2bXxC3hXnGsNQPWej9bvKnRXujzwpd5iooWHdrI00TAEzztS9',
        'client_secret': "test",
    }

    return render(request, template, context)
