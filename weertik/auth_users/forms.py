from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms.widgets import DateInput, Textarea
from django.shortcuts import get_object_or_404


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    email = forms.EmailField()
    email_repeat = forms.EmailField(label="Repeat your email")

    def clean_email(self):
        if self.data['email'] != self.data['email_repeat']:
            raise forms.ValidationError('Los emails no coinciden')
        return self.data['email']

    def clean(self, *args, **kwargs):
        self.clean_email()
        return super(SignupForm, self).clean(*args, **kwargs)
