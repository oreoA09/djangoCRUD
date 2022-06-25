from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list_view, name='all'),
    path("create/", views.post_create_view, name="post_create"),
    path("delete/<slug:slug>", views.post_delete_view, name="post_delete"),
    path("update/<slug:slug>", views.post_update_view, name="post_update"),
    path("read/<slug:slug>", views.post_detail_view, name="post_detail"),
]