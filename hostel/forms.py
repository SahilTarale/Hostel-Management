from dataclasses import field, fields
from django import forms
from .models import student


class studentApplicationForm(forms.ModelForm):
    class Meta:
        model= student
        fields= "__all__"
