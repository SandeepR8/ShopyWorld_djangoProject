from django.urls import path
from . import views

urlpatterns = [
    path('success/',views.payment_success,name='payment_success'),
    path('checkout/<int:pk>',views.single_checkout,name='single_checkout'),
    path('checkout/',views.checkout,name='checkout'),
    path('Billing/',views.Billing,name='billing'),
    path('Process_order/',views.process_order,name="process_order"),
    path('shipped_dash/',views.shipped_dash,name="shipped_dash"),
    path('not_shipped_dash/',views.not_shipped_dash,name="not_shipped_dash"),
    path('order/<int:pk>', views.orders, name='orders'),
    path('order_status',views.Order_status,name='Order_status'),


    
]
