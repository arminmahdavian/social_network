from django.urls import path
from.views import MessageListView, MessageCreateView


app_name = 'messaging'

urlpatterns = [
    path('', MessageListView.as_view(), name = 'messages_list'),
    path('create/', MessageCreateView.as_view(), name = 'create_message'),

]







