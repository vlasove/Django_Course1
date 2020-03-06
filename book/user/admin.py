from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
  model = CustomUser
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  list_display = ['email', 'username', 'year', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)