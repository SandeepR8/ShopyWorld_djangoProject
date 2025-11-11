from django import forms
from .models import CustomerProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['phone', 'zipcode', 'city', 'state', 'country', 'address1', 'address2']
        labels = {field: '' for field in fields}

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Enter Zipcode', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter City', 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter State', 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter Country', 'class': 'form-control'}),
            'address1': forms.Textarea(attrs={'placeholder': 'Enter Address Line 1', 'class': 'form-control', 'rows': 2}),
            'address2': forms.Textarea(attrs={'placeholder': 'Enter Address Line 2 (optional)', 'class': 'form-control', 'rows': 2}),
        }

  