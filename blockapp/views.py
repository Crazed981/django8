from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    post = Article.
    return render(request, 'blockapp/home.html')
