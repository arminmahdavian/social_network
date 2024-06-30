from django.contrib import admin
from .models import Post, PostFile, Comment, Like


# Register your models here.


class PostFileInlineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file',)
    extra = 1



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_active', 'created_at',)
    inlines = [PostFileInlineAdmin]


# class CommentInlineAdmin(admin.TabularInline):
#     model = Comment
#     fields = ('post', 'user', 'text', 'is_approved',)
#     extra = 1

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'is_approved', 'created_at',)
    # inlines = [CommentInlineAdmin]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_liked', 'created_at',)




