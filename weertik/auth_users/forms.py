# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms.widgets import DateInput, Textarea
from django.shortcuts import get_object_or_404


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 label='Nombre')
    last_name = forms.CharField(max_length=30,
                                required=True,
                                label='Apellidos')
    password = forms.CharField(widget=forms.PasswordInput(),
                               required=True,
                               label='Contraseña')
    email = forms.EmailField(label='Correo electrónico')
    email_repeat = forms.EmailField(label='Repite el correo electrónico')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control',
             'required': True,
             'placeholder': 'Nombre'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control',
             'required': True,
             'placeholder': 'Apellidos'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control',
             'required': True,
             'placeholder': 'Contraseña'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control',
             'required': True,
             'placeholder': 'Correo electrónico'})
        self.fields['email_repeat'].widget.attrs.update(
            {'class': 'form-control',
             'required': True,
             'placeholder': 'Repita el correo electrónico'})

    def clean_email(self):
        if self.data['email'] != self.data['email_repeat']:
            raise forms.ValidationError('Los emails no coinciden')
        return self.data['email']

    def clean(self, *args, **kwargs):
        self.clean_email()
        return super(SignupForm, self).clean(*args, **kwargs)
