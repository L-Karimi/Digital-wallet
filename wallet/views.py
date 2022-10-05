from locale import currency
from urllib import request

from .models import Card, Currency, Customer, Loan, Notifications, Receipts, Reward, ThirdParty, Transaction
from .forms import CurencyRegistrationForm, CustomerRegistrationForm, ThridpartyRegistrationForm
from .forms import CardRegistrationForm
from .forms import LoanRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import RewardRegistrationForm
from .forms import TransactionRegistrationForm
from django. shortcuts import render,redirect
from .import models
from .import forms
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
def list_receiptss(request):
    receiptss=Receipts.objects.all()
    return render(request,'wallets/list_receiptss.html',{"receiptss" :receiptss })

def register_reward(request):
    if request.method=="POST":
        form=RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
           form = RewardRegistrationForm()
    return render(request,'wallets/register_reward.html',
                  {"form":form})
def list_rewards(request):
    rewards=Reward.objects.all()
    return render(request,'wallets/list_rewards.html',{"rewards" :rewards })

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
    return render(request,'wallets/list_thirdpartys.html',{"thirdpartys":thirdpartys })

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

    
def customers_profile(request,id):  
    customer=Customer.objects.get(id=id)
    return render(request,"wallets/customers_profile.html" ,{"customers":Customer})

def edit_customer(request,id):
    customer=models.Customer.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/customers_edit.html",{"form":forms})
    
def cards_profile(request,id):  
    card=Card.objects.get(id=id)
    return render(request,"wallets/cards_profile.html" ,{"card":Card})

def edit_card(request,id):
    card=models.Card.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/edit_card.html",{"form":forms})
    
def currencys_profile(request,id):  
    currency=Currency.objects.get(id=id)
    return render(request,"wallets/currency_profile.html" ,{"currency":Currency})

def edit_currency(request,id):
    currency=models.Currency.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/edit_currency.html",{"form":forms})
    
def loan_profile(request,id):  
    loan=Loan.objects.get(id=id)
    return render(request,"wallets/loan_profile.html" ,{"loan":Loan})

def edit_loan(request,id):
    loan=models.Loan.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/edit_loan.html",{"form":forms})
    
def notifications_profile(request,id):  
    notifications=Notifications.objects.get(id=id)
    return render(request,"wallets/notifications_profile.html" ,{"notifications":Notifications})

def edit_notifications(request,id):
    notifications=models.Notifications.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/edit_notifications.html",{"form":forms})
    
def receipts_profile(request,id):  
    receipts=Receipts.objects.get(id=id)
    return render(request,"wallets/receipts_profile.html" ,{"receipts":Receipts})

def edit_receipts(request,id):
    receipts=models.Receipts.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/edit_receipts.html",{"form":forms})
    
def reward_profile(request,id):  
    reward=Reward.objects.get(id=id)
    return render(request,"wallets/reward_profile.html" ,{"reward":Reward})

def edit_reward(request,id):
    reward=models.Reward.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/edit_reward.html",{"form":forms})
    
def thirdparty_profile(request,id):  
    thirdparty=ThirdParty.objects.get(id=id)
    return render(request,"wallets/thirdparty_profile.html" ,{"thirdparty":ThirdParty})

def edit_thirdparty(request,id):
    thirdparty=models.ThirdParty.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/edit_thirdparty.html",{"form":forms})
    
      
def transaction_profile(request,id):  
    transaction=Transaction.objects.get(id=id)
    return render(request,"wallets/transaction_profile.html" ,{"transaction":Transaction})

def edit_transaction(request,id):
    transaction=models.Transaction.objects.get(id=id)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect(request,"wallet/edit_transaction.html",{"form":forms})
    
      
      
      
      
      
      

      

    
