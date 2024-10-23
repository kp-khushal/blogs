from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
from django.db.models import Q
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_result.html'
    fields = '__all__'
    
    def get_queryset(self):
        query = self.request.GET.get('qs')
        #object_list = '__all__'
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(meta_keyword__icontains=query) | Q(content__icontains=query)
        )
        return object_list
         

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    
    
    
