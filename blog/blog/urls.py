from django.urls import path 
from .views import (
  BlogListView,
  PostDetailView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView,
)

urlpatterns = [
  path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
  path('post/new/', PostCreateView.as_view(), name='post_new'),
  path('', BlogListView.as_view(), name='home'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]