from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    billing_same = forms.BooleanField(
        required=False,
        label="Billing address same as shipping",
    )

    class Meta:
        model = ShippingAddress
        fields = [
            "shipping_full_name",
            "shipping_email",
            "shipping_phone",
            "shipping_Address1",
            "shipping_Address2",
            "shipping_city",
            "shipping_state",
            "shipping_zipcode",
            "shipping_country",
        ]
        widgets = {
            
            
            "shipping_country": forms.Select(attrs={
                "class": "form-select"
            }, choices=[
                ("", "Select Country"),
                ("US", "United States"),
                ("CA", "Canada"),
                ("UK", "United Kingdom"),
                ("AU", "Australia"),
                ("DE", "Germany"),
                ("IN", "India"),
                ("RU", "Russia"),
                ("ZA", "South Africa"),
                ("CN", "China"),
                ("TH", "Thailand"),
            ]),
        }
