from django.contrib import admin
from .models import Product,Order,Category,CustomerProfile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'state', 'is_verified', 'date_modified')
    search_fields = ('user__username', 'phone', 'city', 'state', 'zipcode') 
    list_filter = ('is_verified', 'state', 'country') 
    ordering = ('-date_modified',) 
