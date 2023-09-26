from django.shortcuts import render, redirect
from django.views import View
from .models import Subscriber, Product
from .models import Comment

from django.views import View
from django.shortcuts import render, redirect
from .models import Comment  # Импортируйте вашу модель Comment


class CategoryView(View):
    def get(self, request):
        return render(request, 'category.html')


def home(request):
    products = Product.objects.all()[:3]
    return render(request, 'index.html', {'products': products})


def blog(request):
    return render(request, 'blog.html')


def single_blog(request):
    return render(request, 'single-blog.html')


def subscribe_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()

    return redirect('single-blog')


class AddCommentView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        comment_text = request.POST['comment']

        comment = Comment(name=name, email=email, website=website, text=comment_text)
        comment.save()

        return redirect(
            'home')
