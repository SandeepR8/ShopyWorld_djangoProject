from django.shortcuts import render,redirect
from cart.cart import Cart
from .models import ShippingAddress,Order,OrderItem
from django.contrib.auth.decorators import login_required
from .forms import ShippingAddressForm,BillingForm
from django.contrib.auth.models import User
from django.contrib import messages
from decimal import Decimal
from store.models import Product
def payment_success(request):
    return render(request,'payment/payment_success.html')


def shipped_dash(request):
    pass

def not_shipped_dash(request):
    pass

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
            shipping_address.user = request.user 
            shipping_address.save()

            # Optionally handle billing_same checkbox
            billing_same = form.cleaned_data.get("billing_same")
            if billing_same:
                request.session['shipping_id'] = shipping_address.id
                request.session['billing_same'] = form.cleaned_data.get('billing_same')
                
            else:
                # creating seesion for store shipping address for custom use
                request.session['shipping_id'] = shipping_address.id

                

            return redirect('billing')
    else:
        form = ShippingAddressForm()

    return render(request, 'payment/checkout.html', {
        "form": form,
        "cart_products": cart_products,
        "totals": totals,
    })

# Process Order view

def process_order(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    totals = cart.cart_total()
    shipping_id = request.session.get('shipping_id')
    shipping_details = ShippingAddress.objects.get(id=shipping_id)
    
    user=request.user
    full_name = shipping_details.shipping_full_name
    email = shipping_details.shipping_email
    shipping_address = f'{shipping_details.shipping_Address1}\n {shipping_details.shipping_Address2}\n {shipping_details.shipping_state}\n {shipping_details.shipping_city}\n {shipping_details.shipping_zipcode}\n {shipping_details.shipping_country}'
    amount_pay = Decimal(str(totals)) if totals else Decimal("0.00")

    if request.POST:
        payment_form = BillingForm(request.POST or None)

        create_order = Order(user=user, full_name = full_name, email=email, Shipping_Address = shipping_address, amount_pay = amount_pay)
        create_order.save()
        order_id = create_order.pk


        for product in cart_products():
            product_ = product['product']
            product_id = product_.id
            price = product['price']            
            quantity = product['quantity']

            create_order_item = OrderItem(order_id =order_id, product_id =product_id, user_id = user.id, quantity = quantity, price = price)
            create_order_item.save()

        for key in list(request.session.keys()):
            if key == "cart":
                del request.session[key]

        messages.success(request,'Order placed!')
        return redirect('Home')
    
    else :
        create_order = Order(user=user, full_name = full_name, email=email, Shipping_Address = shipping_address, amount_pay = amount_pay)
        create_order.save()
        order_id = create_order.pk


        for product in cart_products():
            product_ = product['product']
            product_id = product_.id
            price = product['price']            
            quantity = product['quantity']

            create_order_item = OrderItem(order_id =order_id, product_id =product_id, user_id = user.id, quantity = quantity, price = price)
            create_order_item.save()

        for key in list(request.session.keys()):
            if key == "cart":
                del request.session[key]


        messages.success(request,'Order placed!')
        return redirect('Home')







def Billing(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    totals = cart.cart_total()
    boolean_element = request.session.get('billing_same')
    if boolean_element :
        shipping_id = request.session.get('shipping_id')
        billing_details = ShippingAddress.objects.get(id=shipping_id)
        billing_form=BillingForm()
        
    else:
        billing_details = None
        billing_form = BillingForm()



    return render(request,'payment/billing.html',{
        "cart_products": cart_products,
        "totals": totals,
        'shipping_details' : billing_details,
        "billing_form" : billing_form
    })

