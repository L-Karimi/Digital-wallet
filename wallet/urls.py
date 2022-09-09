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
    ]
