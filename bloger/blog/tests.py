from django.test import TestCase
from django.urls import reverse 
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Post 

class BlogTest(TestCase):

  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username="testuser",
      email = "user@user.com",
      password="12345678"
    )
    self.post = Post.objects.create(
      title = 'My test post',
      body = 'Body of test post',
      author = self.user,
    )

  def test_post(self):
      self.assertEqual(f'{self.post.title}', 'My test post')
      self.assertEqual(f'{self.post.body}', 'Body of test post')
      self.assertEqual(f'{self.post.author.username}', 'testuser')

  def test_post_detail(self):
      response = self.client.get('/post/1/')
      self.assertEqual(response.status_code , 200)
      self.assertContains(response, 'My test post')
      self.assertTemplateUsed(response, 'post_detail.html')

      response_bad =  self.client.get('/post/3/')
      self.assertEqual(response_bad.status_code , 404)

  def test_post_list(self):
      response = self.client.get(reverse('home'))
      self.assertEqual(response.status_code,200)
      self.assertTemplateUsed(response, 'home.html')
      self.assertContains(response, 'My test post') 
