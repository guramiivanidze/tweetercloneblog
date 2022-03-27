
from turtle import update
from unicodedata import name
from django.urls import path
from .views import AddCategoryView, AddPostView, mypostsView, DeletePostView, HomeView, UpdatePostView, articleDetailView, categoryView, LikeView
urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', articleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', categoryView , name='category'),
    path('like/<int:pk>/', LikeView , name='like_post'),
    path('my_posts/<int:pk>/', mypostsView , name='my_posts'),
]
