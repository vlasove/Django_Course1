from django.shortcuts import render
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
) 

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
