from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from .models import Post
from django.urls import reverse, reverse_lazy
from .forms import PostUpdateForm


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


class PostListView(ListView):
    template_name = 'postlist.html'
    model = Post
    paginate_by = 4


class PostDetailView(DetailView):
    template_name = 'postdetail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Post_list"] = Post.objects.order_by('?')[:6]
        return context


class PostUpdateView(UpdateView):
    template_name = 'postupdate.html'
    model = Post
    form_class = PostUpdateForm
    def get_success_url(self):
        return reverse('chusen:postdetail', kwargs={'pk': self.object.pk})


class UserSettingView(TemplateView):
    template_name = 'usersetting.html'
    model = Post
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["Post_list"] = Post.objects.filter(server=user) 
        return context


class ChusenView(TemplateView):
    template_name = 'chusen.html'
    



class AdaptionView(TemplateView):
    template_name = "adaption.html"
    
    
