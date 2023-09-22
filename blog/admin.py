from django.contrib import admin
from .models import Post, Category, Comment
from .forms import PostAdminForm


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)