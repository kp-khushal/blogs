from django.urls import path
from .views import BlogDetailView, BlogListView, BlogCreateView,SearchResultsView

urlpatterns = [
    path('',BlogListView.as_view(),name='home'),
    path('post/<slug:slug>/',BlogDetailView.as_view(), name='post_detail'),
    path('search/',SearchResultsView.as_view(),name="search_results"),
    path('post_new/',BlogCreateView.as_view(), name='post_new'),
]