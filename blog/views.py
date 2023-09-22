
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
from django.http import HttpResponse

from slugify import slugify
import random

from .models import *
from .forms import *

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    if posts:
        trend_post = Post.objects.all().order_by('-comments')[0]
        trend_intro = trend_post.body[:250]


        context = {
            'posts': posts,
            'trend_post': trend_post,
            'trend_intro': trend_intro,
            }
        return render(request, 'blog/index.html', context)
    else:
        return render(request, 'blog/index.html')
    
def about(request):
    return render(request, 'blog/about.html')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()

    if request.method == 'POST':
        print(request)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentor = request.user
            comment.post = post
            comment.save()

            return redirect('blog:post_detail', slug=slug)

    else:
        form = CommentForm()

    context = {
        'categories': categories,
        'post': post,
        'form': form,
    }

    return render(request, 'blog/post_detail.html', context)


# the code below is to add login_required decorator to class based views
@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    model = Post
    fields = ['category', 'title', 'body', 'image', 'status']
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title + str(form.instance.id))
        return super().form_valid(form)
    
