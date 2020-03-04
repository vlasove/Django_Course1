from django.urls import path 
from .views import BlogListView, PostDetailView

urlpatterns = [
  path('', BlogListView.as_view(), name='home'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]