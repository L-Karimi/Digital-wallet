from django.shortcuts import render
from .forms import CurencyRegistrationForm, CustomerRegistrationForm, ThridpartyRegistrationForm
from .forms import CardRegistrationForm
from .forms import LoanRegistrationForm


from .forms import NotificationRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import RewardRegistrationForm
from .forms import TransactionRegistrationForm



# Create your views here.
def register_customer(request):
    def register_Customer(request):
        if request.method=="POST":
            form=CustomerRegistrationForm(request.POST)
            if form.is_valid();
                form.save()
        else:
            form=CustomerRegistrationForm()
        return render(request, 'customer/customer_registration.html',{'form':form})
    form = CustomerRegistrationForm()
    return render(request,'wallets/register_customer.html',
                  {"form":form})
    
def register_card(request):
    form = CardRegistrationForm()
    return render(request,'wallets/register_card.html',
                  {"form":form})
def register_currency(request):
    form = CurencyRegistrationForm()
    return render(request,'wallets/register_currency.html',
                  {"form":form})
def register_loan(request):
    form = LoanRegistrationForm()
    return render(request,'wallets/register_loan.html',
                  {"form":form})
def register_notification(request):
    form = NotificationRegistrationForm()
    return render(request,'wallets/register_notification.html',
                  {"form":form})
def register_receipt(request):
    form = ReceiptRegistrationForm()
    return render(request,'wallets/register_receipt.html',
                  {"form":form})
def register_reward(request):
    form = RewardRegistrationForm()
    return render(request,'wallets/register_reward.html',
                  {"form":form})
def register_thirdparty(request):
    form = ThridpartyRegistrationForm()
    return render(request,'wallets/register_thirdparty.html',
                  {"form":form})
def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,'wallets/register_transaction.html',
                  {"form":form})
    
            

    
