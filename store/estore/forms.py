from django import forms
from estore.models import Customer

class RegistrationForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    shippingAddress = forms.CharField()
    addressline2 = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    state = forms.CharField()	
    zipCode = forms.CharField()	
    homePhone = forms.IntegerField()
    mobilePhone = forms.IntegerField()
    emailId =  forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
	
    class Meta: Customer	
