from django.shortcuts import render,redirect
from cart.cart import Cart
from .models import ShippingAddress
from django.contrib.auth.decorators import login_required
from .forms import ShippingAddressForm


def payment_success(request):
    return render(request,'payment/payment_success.html')




@login_required
def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    totals = cart.cart_total()
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user  # link to logged-in user
            shipping_address.save()

            # Optionally handle billing_same checkbox
            billing_same = form.cleaned_data.get("billing_same")
            if billing_same:
                # If you want to store billing info same as shipping,
                # you can duplicate or set a flag here.
                pass  

            return redirect('Home')
    else:
        form = ShippingAddressForm()

    return render(request, 'payment/checkout.html', {
        "form": form,
        "cart_products": cart_products,
        "totals": totals,
    })

