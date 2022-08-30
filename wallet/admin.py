from locale import currency
from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Currency
from .models import Account
from .models import Wallet
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notifications
from .models import Receipts
from .models import Reward
from .models import Loan



class CustomerAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','Email',)
    search_fields=('first_name','last_name',)
admin.site.register(Customer,CustomerAdmin)

    
class CurrencyAdmin(admin.ModelAdmin):
    list_display =('amount','country_of_origin',)
    search_fields=('amount','country_of_origin',)
admin.site.register(Currency,CurrencyAdmin)

    
class WalletAdmin(admin.ModelAdmin):
    list_display =('balance','status',)
    search_fields=('balance','status',) 
admin.site.register(Wallet,WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display =('transaction_ref','transaction_type',)
    search_fields=('transaction_ref','transaction_type',)
admin.site.register(Transaction,TransactionAdmin)

    
class CardAdmin(admin.ModelAdmin):
    list_display =('card_name','card_number',)
    search_fields=('card_name','card_number',)
admin.site.register(Card,CardAdmin)
    
    
class ThirdPartyAdmin(admin.ModelAdmin):
    list_display =('account','name','phone_Number',)
    search_fields=('account','name','phone_Number',)  
admin.site.register(ThirdParty,ThirdPartyAdmin)
    
    
class NotificationsAdmin(admin.ModelAdmin):
    list_display =('notification_Id','status','date',)
    search_fields=('notification_Id','status','date',)  
admin.site.register(Notifications,NotificationsAdmin)
    
    
class ReceiptsAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ('receipt_file','receipt_date',)
admin.site.register(Receipts,ReceiptsAdmin)
    
class LoanAdmin(admin.ModelAdmin):
    list_display =('loan_type','amount','due_date',)
    search_fields=('loan_type','amount','due_date',)
admin.site.register(Loan,LoanAdmin)
   
    
class RewardsAdmin(admin.ModelAdmin):
    list_display =('transaction','date','gender',)
    search_fields=('transaction','date','gender',)  
admin.site.register(Reward,ReceiptsAdmin)
    
        
# admin.site.register(Customer,CustomerAdmin)
# admin.site.register(Wallet,WalletAdmin)
# admin.site.register(Currency,CurrencyAdmin)

# admin.site.register(Transaction,TransactionAdmin)
# admin.site.register(Card,CardAdmin)
# admin.site.register(ThirdParty,ThirdPartyAdmin)
# admin.site.register(Notifications,NotificationsAdmin)
# admin.site.register(Receipts,ReceiptsAdmin)
# admin.site.register(Loan,LoanAdmin)
# admin.site.register(Reward,RewardsAdmin)




# admin.site.register(Card,CardAdmin)




# admin.site.register(Currency)

# admin.site.register(Wallet)
# admin.site.register(Transaction)
# admin.site.register(Card)
# admin.site.register(ThirdParty)
# admin.site.register(Notifications)
# admin.site.register(Receipts)
# admin.site.register(Reward)
# admin.site.register(Loan)
# admin.site.register(Account)
