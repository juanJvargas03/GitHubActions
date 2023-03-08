from django import forms
from .models import people

class PeopleForm(forms.ModelForm):
    class Meta:
        model = people