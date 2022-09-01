# from datetime import timezone
from django.utils import timezone
from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    Address=models.TextField()
    Email=models.EmailField()
    Phone_Number=models.CharField(max_length=12,null=True)
    Gender=models.CharField(max_length=7,null=True)
    nationality=models.CharField(max_length=15,null=True)
    Age=models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    date_created = models.DateTimeField(default=timezone.now)
    nationality=models.CharField(max_length=20,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)

class Currency(models.Model):
    amount=models.IntegerField()
    country_of_origin=models.CharField(max_length=24,null=True) 

class Wallet(models.Model):
    currency =models.ForeignKey('Currency', on_delete=models.CASCADE, related_name ='Wallet_currency')
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Wallet_customer')
    balance=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=20,null=True)
    pin=models.TextField(max_length=6,null=True)

class Account(models.Model):
    account_number=models.IntegerField()
    account_type=models.CharField(max_length=20,null=True)
    balance=models.IntegerField()
    name=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name ='Account_wallet')

class Transaction(models.Model):
    transaction_ref=models.CharField(max_length=255,null=True)
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name   = 'Transaction_wallet')
    transaction_amount=models.IntegerField()
    TRANSACTION_CHOICES = (
       ('withdraw', 'Withdrawal'),
        ('depo', 'deposit'),
    )
    transaction_type=models.CharField(max_length=10, choices=TRANSACTION_CHOICES,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    # receipt=models.ForeignKey('Receipts',on_delete=models.CASCADE, related_name='Transaction_receipt')
    original_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_original_account')
    destination_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination_account')

class Card(models.Model):
    date_Issued=models.DateTimeField(default=timezone.now)
    card_name=models.CharField(max_length=20,null=True)
    card_number=models.IntegerField()
    ISSUER_CHOICES=(
         ('Master', 'Mastercard'),
        ('visa', 'visacard'),
    )
    card_type=models.CharField(max_length=10, choices=ISSUER_CHOICES,null=True)
    expiry_date=models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('d', 'debit'),
        ('c', 'credit'),
    )
    
    card_status= models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)
    cvv_security=models.IntegerField()
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='Card_wallet')
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Card_account')     

# <class 'wallet.admin.ReceiptsAdmin'>: (admin.E108) The value of 'list_display[0]' refers to 'receipt_type', which is not a callable, an attribute of 'ReceiptsAdmin', or an attribute or method on 'wallet.Reward'.
class ThirdParty(models.Model):
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='ThirdParty_account')
    name=models. CharField(max_length=15,null=True)
    thirdparty_id=models.CharField(max_length=10,null=True)
    phone_Number=models.IntegerField()
    currency=models.ForeignKey('Currency', on_delete=models.CASCADE, related_name ='ThirdParty_currency')

class Notifications(models.Model):
 notification_Id=models.CharField(max_length=25,null=True)
 STATUS_CHOICES = (
        ('read', 'read'),
        ('unread', 'unread'),
    )
 status=models.CharField(max_length=12, choices=STATUS_CHOICES,null=True)
 date=models.DateTimeField(default=timezone.now)
 recipient=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Notifications_recipient')    
 
class Receipts(models.Model):
    receipt_type=models.CharField(max_length=25, null=True)
    receipt_date=models.DateTimeField(default=timezone.now)
    receipt_number=models.CharField(max_length=25, null=True)
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Receipts_account')
    total_Amount=models.IntegerField(default=0)
    # transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Receipts_transaction')
    receipt_File=models.FileField(upload_to='wallet/')

class Loan(models.Model):
 loan_number=models.IntegerField()
 loan_type=models.CharField(max_length=25, null=True)
 amount=models.IntegerField()
 date=models.DateTimeField(default=timezone.now)
 wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='Loan_wallet')
 interest_rate=models.IntegerField()
 guaranter=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Loan_guaranter')
 due_date=models.DateTimeField(default=timezone.now)
 loan_balance=models.IntegerField()
 loan_term=models.IntegerField()


class Reward(models.Model):  
 transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Reward_transaction')
 date=models.DateTimeField(default=timezone.now)
 customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Reward_customer')
 GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
 gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)  
 bonus=models.CharField(max_length=25, null=True)
 
