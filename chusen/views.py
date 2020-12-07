from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class TopView(TemplateView):
    template_name = "top.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["isnt_title_bar"] = True
        return context

class HomeView(TemplateView):
    template_name = "home.html"


class AdaptionView(TemplateView):
    template_name = "adaption.html"
    
    
