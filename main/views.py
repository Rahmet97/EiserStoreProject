from django.shortcuts import render
from django.views import View

from .models import Product


class CategoryView(View):
    def get(self, request):
        return render(request, 'category.html')


def home(request):
    return render(request, 'index.html')


class SingleProductView(View):

    def post(self, request):
        id = request.GET.get('id')
        product = Product.objects.get(id=id)
        return render(request, 'single-product.html', {'product': product})
