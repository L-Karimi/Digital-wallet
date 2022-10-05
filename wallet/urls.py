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

    path('customers/<int:id>/', views.customers_profile, name="customers_profile"),
    path('customers/edit/<int:id>/',views.edit_customer, name="edit_customer"),
    
    path('cards/<int:id>/', views.cards_profile, name="cards_profile"),
    path('cards/edit/<int:id>/',views.edit_card, name="edit_card"),
    
    path('currencys/<int:id>/', views.currencys_profile, name="currencys_profile"),
    path('currencys/edit/<int:id>/',views.edit_currency, name="edit_currency"),
    
    path('loan/<int:id>/', views.loan_profile, name="loan_profile"),
    path('loan/edit/<int:id>/',views.edit_loan, name="edit_loan"),
    
    path('notifications/<int:id>/', views.notifications_profile, name="notifications_profile"),
    path('notifications/edit/<int:id>/',views.edit_notifications, name="edit_notifications"),
    
    path('receipts/<int:id>/', views.receipts_profile, name="receipts_profile"),
    path('receipts/edit/<int:id>/',views.edit_receipts, name="edit_receipts"),
    
    path('reward/<int:id>/', views.reward_profile, name="reward_profile"),
    path('reward/edit/<int:id>/',views.edit_reward, name="edit_reward"),
    
    path('thirdparty/<int:id>/', views.thirdparty_profile, name="thirdparty_profile"),
    path('thirdparty/edit/<int:id>/',views.edit_thirdparty, name="edit_thirdparty"),
    
    path('transaction/<int:id>/', views.transaction_profile, name="transaction_profile"),
    path('transaction/edit/<int:id>/',views.edit_transaction, name="edit_transaction"),
    ]
