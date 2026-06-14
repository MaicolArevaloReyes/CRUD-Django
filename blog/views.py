from django.shortcuts import render
from django.views.generic import ListView, DetailView,  CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post   
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

# Create your views here.

#visualizar la lista
class PostListView (ListView):
    model = Post    
    template_name = 'blog/post_list.html'
    
#modificar la lista creo
class PostDetailView (DetailView):  
    model = Post
    template_name = 'blog/post_detail.html'
    
#crear una lista
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
#eliminar una lista    
class PostDeleteView (DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy ('post-list')
    
#modificar una lista 

class PostUpdateView (LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy ('post-list')
