from django.shortcuts import render
from .models import Post

posts = [
    {
        'author' : 'Diego',
        'title' : 'Blog post 1',
        'content' : 'Primer Contenido del Post',
        'date_posted' : 'Noviembre 06, 2020'
    },
    {
        'author' : 'Juan',
        'title' : 'Blog post 2',
        'content' : 'Segundo Contenido del Post',
        'date_posted' : 'Noviembre 06, 2020'
    }

]

# Create your views here.

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'Sobre Nosotros'})
