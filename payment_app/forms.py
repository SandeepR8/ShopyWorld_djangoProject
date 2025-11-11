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



class BillingForm(forms.Form):
    billing_full_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Full Name'})) 
    billing_email = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
    billing_phone = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Phone'}))
    billing_Address1 = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Address1'}))
    billing_Address2 = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Address2 (optional)'}),required=False)
    billing_city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'City'}))
    billing_state = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'State'}),required=False)
    billing_zipcode = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Zip Code'}),required=False)
    billing_country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Country'}))
    
