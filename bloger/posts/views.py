from django.shortcuts import render
from django.contrib.auth.mixins import (
  LoginRequiredMixin,
  UserPassesTestMixin,
)

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
class PostListView(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'posts/posts_list.html'
  context_object_name = 'posts_list' 
  login_url = 'login'

class PostDetailView(LoginRequiredMixin, DetailView):
  model = Post
  template_name = 'posts/post_detail.html'
  context_object_name = 'post'
  login_url = 'login'

class PostEditView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
  model = Post
  template_name = 'posts/post_edit.html'
  fields = ('title', 'body')
  context_object_name = 'post'
  login_url = 'login'
  
  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
  model = Post
  success_url = reverse_lazy('posts_list') 
  template_name = 'posts/post_delete.html'
  login_url = 'login'

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user


class PostNewView(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'posts/post_new.html'
  fields = ('title', 'body')
  context_object_name ='post'
  login_url = 'login'

  def form_valid(self, form):
    form.instance.author = self.request.user 
    return super().form_valid(form)






