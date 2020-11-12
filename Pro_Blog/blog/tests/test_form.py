from django.test import TestCase
from blog.models import Post
from Usuarios.forms import UserRegisterForm


class UserRegisterFormCase(TestCase):

    def test_valid_form(self):
        data = {'username': 'Diego1', 'email' : 'Diego1@gmail.com', 'password1': 'Diego123', 'password2' : 'Diego123' , }
        form = UserRegisterForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        data = {'username': '', 'email' : '', 'password1': 'Diego123', 'password2': 'Diego123', }
        form = UserRegisterForm(data=data)
        self.assertFalse(form.is_valid())
