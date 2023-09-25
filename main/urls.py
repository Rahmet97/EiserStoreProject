from django.urls import path
from django.urls import path

from .views import CategoryView, home

urlpatterns = [
    path('category', CategoryView.as_view, name='category'),
    path('', home())
]