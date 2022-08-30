from Django .urls import path
from .views import register_customer


urlpatterns=[path("register/",register_customer,name="registration"),
             ]
