from django.urls import path 
from .views import (
  PostNewView,
  PostEditView,
  PostDetailView,
  PostDeleteView,
  PostListView,
)

urlpatterns = [
  path('', PostListView.as_view(), name='posts_list'),
  path('new/', PostNewView.as_view(), name='post_new'),
  path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
  path('<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
  path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]