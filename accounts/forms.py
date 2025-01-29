# IMPORT BUILT-IN LIBRARIES
from django import forms

from .models import Profile


class AccountForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('firstname', 'lastname')
