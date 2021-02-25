from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class About(TemplateView):
    template_name = 'about.html'