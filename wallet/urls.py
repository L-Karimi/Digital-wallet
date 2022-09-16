from pydoc import visiblename
from django .urls import path
from. import views


urlpatterns=[
    path("register/",views.register_Customer,name="registration"),
    path("card/",views.register_card,name="card"),
    path("currency/",views.register_currency,name="currency"),
    path("loan/",views.register_loan,name="loan"),
    path("notification/",views.register_notification,name="notification"),
    path("receipt/",views.register_receipt,name="receipt"),
    path("reward/",views.register_reward,name="reward"),
    path("thirdparty/",views.register_thirdparty,name="thirdparty"),
    path("transaction/",views.register_transaction,name="transaction"),
    
    path("customers/",views.list_customers,name="customers"),
    path("cards/",views.list_cards,name="cards"),
    path("currencys/",views.list_currencys,name="currencys"),
    path("loans/",views.list_loans,name="loans"),
    path("notifications/",views.list_notifications,name="notifications"),
    path("receipts/",views.list_receiptss,name="receipts"),
    path("rewards/",views.list_rewards,name="rewards"),
    path("thirdpartys/",views.list_thirdpartys,name="thirdpartys"),
    path("transactions/",views.list_transactions,name="transactions"),
    # path("customers",views.list_customers,name="customers"),
    ]
