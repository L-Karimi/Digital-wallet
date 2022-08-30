from django.shortcuts import render

from wallet.models import Wallet
from .forms import CustomerRegistrationForm

# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,Wallet/register_customer.html,
                  {"form":form})
            

    
