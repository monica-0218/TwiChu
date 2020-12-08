from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

class TopView(TemplateView):
    template_name = "top.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["isnt_title_bar"] = True
        return context

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Post_list"] = Post.objects.order_by('?')[:5]
        return context

class AdaptionView(TemplateView):
    template_name = "adaption.html"
    
    
