from django.urls import path
from .views import (PostListView, 
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView, 
                    PostDeleteView,
                    UserPostListView)
from . import views

urlpatterns = [
    # when we use the class based view we can't pass the view just like PostListView, it has to converted into an actual view to do that use as_view() method
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # here the code inside <> is variable ie it changes according to circumstances. and that int part specifies what type of value it expects here it's integer. it's optional step
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
