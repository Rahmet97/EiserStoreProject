from django.urls import path

from .views import CategoryView, home, S

urlpatterns = [
    path('category', CategoryView.as_view, name='category'),
    path('', home),
    path('single-product', )
]
