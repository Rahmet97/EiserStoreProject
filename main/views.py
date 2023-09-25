from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from .form import CommentForm, NewsletterForm

from .models import Newsletter, Comment


# Create your views here.


class Home(View):
    def get(self, request):
        newsletters = Newsletter.objects.all()

        return render(request, 'index.html', {'newsletters': newsletters})

    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            newsletter = Newsletter.objects.create(
                email=email
            )
            newsletter.save()
        return redirect('/')


class Contact(LoginRequiredMixin, View):

    def get(self, request):
        form = CommentForm()
        comments = Comment.objects.all()
        return render(request, 'contact.html', {'form': form, 'comments': comments})

        # return render(request, 'contact.html', {'comments': comments})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get('message')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')

            newpost = Comment.objects.create(
                message=message,
                name=name,
                email=email,
                subject=subject
            )
            newpost.save()

        # sent new post

            msg = f'''
    {subject}

    {message}

    Full name: {name}
    Email: {email}
            '''
            send_mail(
                'New message',
                msg,
                name,
                ['nqobulov571@gmail.com']
            )
        return redirect('/')
