from django.urls import path
from .views import UserListView, RequestView, RequestListView, AcceptView, FriendListView

app_name = 'friendship'

urlpatterns = [
    path('list/', UserListView.as_view(), name='user_list'),
    path('request/', RequestView.as_view(), name='friend_request'),
    path('requests-list/', RequestListView.as_view(), name='requests_list'),
    path('accept/', AcceptView.as_view(), name='accept_request'),
    path('friends/', FriendListView.as_view(), name='friends_list'),

]





