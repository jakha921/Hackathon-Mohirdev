from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog

# Create your views here.
class HomePageView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    
class HomeDetailsView(DetailView):
    model = Blog
    template_name = 'blog/details.html'
    context_object_name = 'blog'

class HomeCreateView(CreateView):
    model = Blog
    template_name = 'blog/create.html'
    fields = '__all__'
    success_url = '/'

class HomeUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/update.html'
    fields = '__all__'
    success_url = '/'

class HomeDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/delete.html'
    context_object_name = 'blog'
    success_url = '/'
