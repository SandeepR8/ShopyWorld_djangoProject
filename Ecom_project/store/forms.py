from django import forms
from .models import CustomerProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=CustomerProfile
        fields=['phone','address1','address2','city','state','zipcode','country']
        labels = {field: '' for field in fields} 

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number', 'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'placeholder': 'Enter address line 1', 'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'placeholder': 'Enter address line 2 (optional)', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city', 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter state', 'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Enter zipcode', 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country', 'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['phone'].required = True
            self.fields['address2'].required = False

            