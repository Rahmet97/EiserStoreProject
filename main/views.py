from django.shortcuts import render
from django.views import View


class CategoryView(View):
    def get(self, request):
        return render(request, 'category.html')


def home(request):
    return render(request, 'index.html')
