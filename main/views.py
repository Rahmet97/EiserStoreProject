from django.shortcuts import render, redirect
from .models import Subscriber
def home(requset):
    return render(requset, 'index.html')
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


from .models import Comment


from django.views import View
from django.shortcuts import render, redirect
from .models import Comment  # Импортируйте вашу модель Comment

class AddCommentView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        comment_text = request.POST['comment']

        comment = Comment(name=name, email=email, website=website, text=comment_text)
        comment.save()

        return redirect('home')  # Предположим, что 'home' - это имя URL, на которое вы хотите перейти после сохранения комментария.



