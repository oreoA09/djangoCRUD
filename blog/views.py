from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post

# Create your views here.
def PostListView(request):
    model = Post

def PostCreateView(request):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

def PostDetailView(request):
    model = Post

def PostUpdateView(request):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

def PostDeleteView(request):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')