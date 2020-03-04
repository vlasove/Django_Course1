from django.shortcuts import render
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)
from django.urls import reverse_lazy

from .models import Post 

# Create your views here.

class BlogListView(ListView):
  model = Post 
  template_name = 'home.html'
  context_object_name ='all_posts'

class PostDetailView(DetailView):
  model = Post 
  template_name = 'post_detail.html'
  context_object_name = 'post'

class PostCreateView(CreateView):
  model = Post 
  template_name = 'post_new.html'
  fields = ['author', 'title', 'body']
  context_object_name = 'post'

class PostUpdateView(UpdateView):
  model = Post 
  template_name = 'post_update.html'
  fields = ['title', 'body']
  context_object_name = 'post'

class PostDeleteView(DeleteView):
  model = Post 
  template_name = 'post_delete.html'
  success_url = reverse_lazy('home')
  context_object_name = 'post'


