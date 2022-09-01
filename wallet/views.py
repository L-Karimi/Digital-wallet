from django.shortcuts import render
from .forms import CustomerRegistrationForm

# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,'wallets/register_customer.html',
                  {"form":form})

            

    
