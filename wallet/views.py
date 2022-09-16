from locale import currency
from urllib import request
from django.shortcuts import render

from .models import Card, Currency, Customer, Loan, Notifications, Receipts, Reward, ThirdParty, Transaction
from .forms import CurencyRegistrationForm, CustomerRegistrationForm, ThridpartyRegistrationForm
from .forms import CardRegistrationForm
from .forms import LoanRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import RewardRegistrationForm
from .forms import TransactionRegistrationForm



# Create your views here.
def register_Customer(request):
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request, 'wallets/register_customer.html',{'form':form})

def list_customers(request):
    customers=Customer.objects.all()
    return render(request,'wallets/list_customers.html',{"customers" :customers })
 
def register_card(request):
    if request.method=="POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=CardRegistrationForm()
    return render(request,'wallets/register_card.html',{'form':form})
def list_cards(request):
    cards=Card.objects.all()
    return render(request,'wallets/list_cards.html',{"cards" :cards })

    
def register_currency(request):
    if request.method=="POST":
        form = CurencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=CurencyRegistrationForm()
    return render(request,'wallets/register_currency.html',
                  {"form":form})
def list_currencys(request):
    currencys=Currency.objects.all()
    return render(request,'wallets/list_currencys.html',{"currencys" :currencys })

def register_loan(request):
    if request.method=="POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=LoanRegistrationForm()
    return render(request,'wallets/register_loan.html',
                  {"form":form})
def list_loans(request):
    loans=Loan.objects.all()
    return render(request,'wallets/list_loans.html',{"loans" :loans })

def register_notification(request):
    if request.method=="POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=NotificationRegistrationForm()
    return render(request,'wallets/register_notification.html',
                  {"form":form})
def list_notifications(request):
    notifications=Notifications.objects.all()
    return render(request,'wallets/list_notifications.html',{"notifications" :notifications })

    
def register_receipt(request):
    if request.method=="POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=ReceiptRegistrationForm()
    return render(request,'wallets/register_receipt.html',
                  {"form":form})
def list_receipts(request):
    receipts=Receipts.objects.all()
    return render(request,'wallets/list_receipt.html',{"receipts" :receipts })

def register_reward(request):
    if request.method=="POST":
        form=RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
           form = RewardRegistrationForm()
    return render(request,'wallets/register_reward.html',
                  {"form":form})
def list_rewardss(request):
    rewards=Reward.objects.all()
    return render(request,'wallets/list_rewardss.html',{"rewards" :rewards })

def register_thirdparty(request):
    if request.method=="POST":
        form = ThridpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=ThridpartyRegistrationForm()
    return render(request, 'wallets/register_thirdparty.html',{'form':form})
def list_thirdpartys(request):
    thirdpartys=ThirdParty.objects.all()
    return render(request,'wallets/list_thirdpartys.html',{"thirdpartys" :thirdpartys })

def register_transaction(request):
    if request.method=="POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=TransactionRegistrationForm()
    return render(request,'wallets/register_transactions.html',
                  {"form":form})
def list_transactions(request):
    transactions=Transaction.objects.all()
    return render(request,'wallets/list_transactions.html',{"transactions" :transactions })

    
            

    
