from django .urls import path
from .views import register_customer,register_card,register_currency,register_loan,register_notification,register_receipt,register_reward,register_thirdparty,register_transaction


urlpatterns=[
    path("register/",register_customer,name="registration"),
    path("register/",register_card,name="card"),
    path("register/",register_currency,name="currency"),
    path("register/",register_loan,name="loan"),
    path("register/",register_notification,name="notification"),
    path("register/",register_receipt,name="receipt"),
    path("register/",register_reward,name="reward"),
    path("register/",register_thirdparty,name="thirdparty"),
    path("register/",register_transaction,name="transaction"),

    ]
