
from django import forms
from .models import Card, Currency, Customer, Loan, Notifications, Receipts, Reward, ThirdParty, Transaction

class CustomerRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Customer
        fields= "__all__"
        
class CardRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Card
        fields= "__all__"
        
class CurencyRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Currency
        fields= "__all__"
        
class LoanRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Loan
        fields= "__all__"
        
class NotificationRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Notifications
        fields= "__all__"
        
class RewardRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Reward
        fields= "__all__"
        
class ReceiptRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Receipts
        fields= "__all__"
        
class ThridpartyRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=ThirdParty
        fields= "__all__"
        
class TransactionRegistrationForm(forms.ModelForm  ):
    class Meta:#provides data from the inherited data class
        model=Transaction
        fields= "__all__"