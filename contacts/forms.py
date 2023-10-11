from django import forms
from django.forms import inlineformset_factory
from .models import Contact, PhoneNumber


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name']


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number']


PhoneNumberFormSet = inlineformset_factory(Contact, PhoneNumber, form=PhoneNumberForm, extra=1)
