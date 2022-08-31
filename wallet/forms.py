
from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Customer
        fields= "__all__"