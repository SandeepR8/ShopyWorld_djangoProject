from store.models import Product,CustomerProfile


class Cart():
	def __init__(self, request):
		self.session = request.session
		# Get request
		self.request = request
		# Get the current session key if it exists
		cart = self.session.get('cart')

		# If the user is new, no session key!  Create one!
		if not cart:
			cart = self.session['cart'] = {}


		# Make sure cart is available on all pages of site
		self.cart = cart

	def db_add(self,product,quantity):
		product_id=str(product)
		product=Product.objects.get(id=product_id)
		if product.sale:
			if product_id not in self.cart:
				self.cart[product_id] = {'quantity': 0, 'price': str(product.sale_price)} 
				self.cart[product_id]['quantity']+=quantity
				self.save()

		else:
			if product_id not in self.cart:
				self.cart[product_id] = {'quantity': 0, 'price': str(product.price)} 
				self.cart[product_id]['quantity']+=quantity
				self.save()
		# adding cart data to user model to authenticated user
		if self.request.user.is_authenticated:
			current_user = CustomerProfile.objects.filter(user__id=self.request.user.id)
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")

			current_user.update(old_cart=str(carty))
		
	
	def add(self, product, quantity=1):
		product_id=str(product.id)
		product=Product.objects.get(id=product_id)
		if product.sale:
			if product_id not in self.cart:
				self.cart[product_id] = {'quantity': 0, 'price': str(product.sale_price)} 
				self.cart[product_id]['quantity']+=quantity
				self.save()

		else:
			if product_id not in self.cart:
				self.cart[product_id] = {'quantity': 0, 'price': str(product.price)} 
				self.cart[product_id]['quantity']+=quantity
				self.save()
		# adding cart data to user model to authenticated user
		if self.request.user.is_authenticated:
			current_user = CustomerProfile.objects.filter(user__id=self.request.user.id)
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")

			current_user.update(old_cart=str(carty))


	def save(self):
		self.session['cart'] = self.cart
		self.session.modified = True

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())
	
	def cart_total(self):
		return sum(float(item['price'])*item['quantity'] for item in self.cart.values())
	
	def get_prods(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		cart = self.cart.copy()
		for product in products:
			cart_item = cart[str(product.id)]
			cart_item['product'] = product
			cart_item['total_price'] = float(cart_item['price']) * cart_item['quantity']
			yield cart_item

	def update(self, product, quantity):
		product_id = str(product.id) if hasattr(product, "id") else str(product)
		if product_id in self.cart:
			self.cart[product_id]['quantity'] = quantity
		self.save()

	def delete(self, product):
		product_id = str(product)

		if product_id in self.cart:
			del self.cart[product_id]
		self.save()

		# profile = CustomerProfile.objects.get(user__id = self.request.user.id)
		# items = json.loads(profile.old_cart)
		# if str(product_id) in items:
		# 	del items[str(product_id)]
		