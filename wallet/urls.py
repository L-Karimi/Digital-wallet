from django .urls import path
from .views import register_customer,register_card,register_currency,register_loan,register_notification,register_receipt,register_reward,register_thirdparty,register_transaction


urlpatterns=[
    path("register/",register_customer,name="registration"),
    path("card/",register_card,name="card"),
    path("currency/",register_currency,name="currency"),
    path("loan/",register_loan,name="loan"),
    path("notification/",register_notification,name="notification"),
    path("receipt/",register_receipt,name="receipt"),
    path("reward/",register_reward,name="reward"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("transaction/",register_transaction,name="transaction"),

    ]
