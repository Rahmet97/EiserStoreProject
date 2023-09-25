from django.urls import path

from .views import CategoryView, home

urlpatterns = [
    path('', home, name='home'),
    path('category', CategoryView.as_view(), name='category')
]

