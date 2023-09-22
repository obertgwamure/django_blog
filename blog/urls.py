from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('new-post/', CreatePostView.as_view(), name='create_post'),
    path('blog/<slug:slug>', post_detail, name='post_detail'),
    path('about', about, name='about'),
    path('', home, name='home'),
]