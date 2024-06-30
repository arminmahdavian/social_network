from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('new', views.PostView.as_view(), name='new_post'),
    path('list', views.PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostView.as_view(), name='post_detail'),
    path('<int:pk>/comments/', views.CommentView.as_view(), name='comment'),
    path('<int:pk>/likes/', views.LikeView.as_view(), name='like'),

]









