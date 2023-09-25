from django.urls import path

from main.views import Home, Contact

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contact/', Contact.as_view(), name='contact')
]
