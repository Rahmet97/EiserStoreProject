from django.urls import path
from .views import home, blog, single_blog, subscribe_form, AddCommentView, CategoryView

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('single-blog/', single_blog, name='single-blog'),
    path('subscribe/', subscribe_form, name='subscribe_form'),
    path('add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('category', CategoryView.as_view(), name='category')
]
