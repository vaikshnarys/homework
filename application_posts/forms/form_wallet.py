from django import forms
from application_posts.models import *

class AddWalletForm(forms.Form):
    name = forms.CharField(max_length=200, label = 'Name wallet')
    currency = forms.CharField(max_length=200, label = 'Currency')
    balance = forms.FloatField(max_value=100000, label = 'Balance')
