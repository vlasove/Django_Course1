from django.test import TestCase, SimpleTestCase
from django.urls import reverse 
from django.contrib.auth import get_user_model

# Create your tests here.
class HomePageTests(SimpleTestCase):

  def test_HP_status_code(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200) 

  def test_HP_BY_NAME_status_code(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)

  def test_HP_RIGHT_TEMPLATE(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
  username = 'testuser'
  email = 'testuser@mail.com'
  
  

  def test_SIGNUP_form(self):
    new_user = get_user_model().objects.create_user(
      self.username, self.email
    )

    self.assertEqual(get_user_model().objects.all().count(), 1)
    self.assertEqual(get_user_model().objects.all()[0].username, self.username)
    self.assertEqual(get_user_model().objects.all()[0].email, self.email)
    

  def test_SIGNUP_status_code(self):
    response = self.client.get('/accounting/signup/')
    self.assertEqual(response.status_code, 200)

  def test_SIGNUP_BY_NAME_status_code(self):
    response = self.client.get(reverse('signup'))
    self.assertEqual(response.status_code, 200)
  
  def test_SIGNUP_RIGHT_TEMPLATE(self):
    response = self.client.get(reverse('signup'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'signup.html')


