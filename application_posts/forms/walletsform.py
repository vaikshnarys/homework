from django import forms
from django.core.exceptions import ValidationError

from application_posts.models import *

class Walletsform(forms.ModelForm):
    class Meta:
        model = Wallettest
        fields = ['name','currency','balance']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-input'}),
            'currency' : forms.TextInput(attrs={'class' : 'form-input'}),
        }
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 10:
            raise ValidationError('Length is exceed limit')
        return name