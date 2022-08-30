from dataclasses import fields
from pyexpat import model
from Django import forms
from .models import Customer
class CustomerRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Customer
        fields="__all_"