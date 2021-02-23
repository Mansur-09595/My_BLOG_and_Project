from django.views.generic import TemplateView


class BlogListView(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'