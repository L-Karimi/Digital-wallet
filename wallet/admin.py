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



admin.site.register(Customer)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notifications)
admin.site.register(Receipts)
admin.site.register(Reward)
admin.site.register(Loan)
