from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
def post_list_view(request):

    model = Post

    return render(request, 'blog/post_list_view.html', {})

def post_create_view(request):

    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

    return render(request, 'post_form_view.html', {})

def post_detail_view(request):

    model = Post
    return render(request, 'post_detail_view.html', {})

def post_update_view(request):

    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

    return render(request, 'post_form_view.html', {})

def post_delete_view(request):

    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

    return render(request, 'post_delete_view.html', {})