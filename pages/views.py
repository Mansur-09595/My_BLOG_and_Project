from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class CreatePostView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class About(TemplateView):
    template_name = 'about.html'