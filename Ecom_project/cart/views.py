from django.shortcuts import render, get_object_or_404,redirect
from .cart import Cart
from store.models import Product,CustomerProfile
from django.http import JsonResponse
from django.contrib import messages
import json

def cart_summary(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	# quantities = cart.get_quants
	totals = cart.cart_total()
	return render(request, "cart/cart_view.html", {"cart_products":cart_products, "totals":totals})



def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty',1))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)
		response = JsonResponse({'Product Name: ': product.name,'cart_length':len(cart)})
		messages.success(request, "Product added to cart!")
		return response

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
	# 	# Get stuff
		product_id = int(request.POST.get('product_id'))
	# 	# Call delete Function in Cart
		cart.delete(product=product_id)
		response = JsonResponse({'product':product_id})
		messages.success(request, "item deleted from cart..")
		return response

	return redirect('cart_summary')
	
	# 	messages.success(request, ("Item Deleted From Shopping Cart..."))
	


def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
	# 	# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		messages.success(request, "Cart is updated..")
		return response

	return redirect('cart_summary')
	# 	messages.success(request, ("Your Cart Has Been Updated..."))
	
