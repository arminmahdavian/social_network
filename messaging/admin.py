from django.contrib import admin
from.models import Message

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'created_at', 'is_read',)
    list_filter = ('is_read', 'created_at',)
    search_fields = ('sender__username', 'receiver__username', 'content',)
    read_fields = ('created_at',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('sender', 'receiver')
        return queryset






