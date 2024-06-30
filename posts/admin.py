from django.contrib import admin
from .models import Post, PostFile


# Register your models here.


class PostFileInlineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file',)
    extra = 1



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_active', 'created_at',)
    inlines = [PostFileInlineAdmin]


# @admin.register(PostFile)
# class PostFileAdmin(admin.ModelAdmin):
#     pass





