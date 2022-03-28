from dataclasses import field
from pyexpat import model
from re import template
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from importlib_metadata import requires
from .forms import PostForm, UpdatePostForm
from .models import Category, Post
from django.http import HttpResponseRedirect


# Create your views here.

# def home (request):
#     return render(request, 'home.html', {})

def LikeView (request, pk ):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    
    liked = False
    
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    cats = Category.objects.all()

    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()

        context = super(HomeView, self).get_context_data(*args, **kwargs)
        
        
        context["cat_menu"] = cat_menu
        return context






def categoryView(request, cats ):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'category_posts': category_posts,
                                               'cats': cats,
                                               })


def mypostsView(request, pk ):
    my_posts = Post.objects.filter(author_id=pk)
    return render(request, 'my_post.html', {'my_posts': my_posts,
                                               })

    
    
    
class articleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()

        context = super(articleDetailView, self).get_context_data(
            *args, **kwargs)
        
        
        stuff  = get_object_or_404(Post, id =self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        
        context["total_likes"] = total_likes
        context["cat_menu"] = cat_menu
        context["liked"] = liked
        
        return context
        

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()
        
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        
        
        
        
        context["cat_menu"] = cat_menu
        
        return context


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()

        context = super(AddCategoryView, self).get_context_data(
            *args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdatePostView (UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()

        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeletePostView (DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()

        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
