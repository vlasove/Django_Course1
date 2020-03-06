from django.shortcuts import render
from django.views.generic import (
  CreateView,
  UpdateView,
  DetailView,
  DeleteView,
  ListView,
)
from .models import Post 
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
  model = Post
  template_name = 'posts/posts_list.html'
  context_object_name = 'posts_list' 

class PostDetailView(DetailView):
  model = Post
  template_name = 'posts/post_detail.html'
  context_object_name = 'post'

class PostEditView(UpdateView):
  model = Post
  template_name = 'posts/post_edit.html'
  fields = ('title', 'body')
  context_object_name = 'post'

class PostDeleteView(DeleteView):
  model = Post
  success_url = reverse_lazy('posts_list') 
  template_name = 'posts/post_delete.html'


class PostNewView(CreateView):
  model = Post
  template_name = 'posts/post_new.html'
  fields = ('title', 'body', 'author')








