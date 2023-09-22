import os
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from autoslug import AutoSlugField #used to generate slug from title


CATEGORY_CHOICES = [
    ('Software Development', 'Software Development'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Tech in Africa', 'Tech in Africa'),
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('JavaScript', 'JavaScript'),
    ('HTML and CSS', 'HTML and CSS'),
    ('Tutorials', 'Tutorials'),
    ('General Tech', 'General Tech'),
    ('Industry-Specific Tech', 'Industry-Specific Tech'),

]

class Category(models.Model):
    title = models.CharField(choices=CATEGORY_CHOICES, max_length=240)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title
    

STATUS_CHOICES = [
    ('complete', 'complete'),
    ('draft', 'draft'),
]

# generating unique file names for image uploads
def post_image_path(instance, filename):
    filename = os.path.basename(slugify(filename))  # remove any directory paths from filename
    return (f'images/{instance.id or 1}/{filename}')

# Create your models here.
class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, default='General Tech')
    title = models.CharField(max_length=240, unique=True)
    body = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField(upload_to='post_image_path', blank=True, max_length=1000)
    status = models.CharField(choices=STATUS_CHOICES, blank=False, default='draft', max_length=15)
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
    
class Comment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.commentor}\'s comment at {self.date}'
    
class SubComment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    Comment = models.ForeignKey(Comment, related_name='subcomments', on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.commentor}\'s comment at {self.date}'

