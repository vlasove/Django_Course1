from django.urls import path 
from .views import BlogListView, PostDetailView, PostCreateView

urlpatterns = [
  path('post/new/', PostCreateView.as_view(), name='post_new'),
  path('', BlogListView.as_view(), name='home'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]