from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# use small bracket to import in multiple line
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'posts': Post.objects.all()  # gets all the data from post table and stores in variable posts. this variabel is used in template to display the data
    }
    return render(request, 'blog/home.html', context)



class PostListView(ListView):  # inheriting from listview 
    # inside this view we need to define a variable called model to tell listview which model it should query (ie display)
    model = Post  

    # - by default class based views look for template with a certain naming pattern:  <app>/<model>_viewtype.html. in this case it is looking for blog/post_list.html where appname is blog, model is post and viewtype is list. we can override this by ecplicitly defining which template it should look for as follows:
    template_name = 'blog/home.html'

    # this view don't know which variable it should loop for to display the blog content. previously we did this by defining a variable called context which passed them variables as a dctionary
    #by default our listview is gonna called that variable object_list. so you can change the variable name from post to object_list or you can define your own variable to override it. we can override this by modifying PostListView as:
    context_object_name = 'posts'

    # currently our list view is displaying the first ie oldest post at top. we want the exact opposite so for that write:
    ordering = ['-date_posted']  # negative sign means show the newest dated post at top

    # defining the number of posts to show per page
    paginate_by = 5


class UserPostListView(ListView):  # inheriting from listview 
    # inside this view we need to define a variable called model to tell listview which model it should query (ie display)
    model = Post  

    # - by default class based views look for template with a certain naming pattern:  <app>/<model>_viewtype.html. in this case it is looking for blog/post_list.html where appname is blog, model is post and viewtype is list. we can override this by ecplicitly defining which template it should look for as follows:
    template_name = 'blog/user_posts.html'

    # this view don't know which variable it should loop for to display the blog content. previously we did this by defining a variable called context which passed them variables as a dctionary
    #by default our listview is gonna called that variable object_list. so you can change the variable name from post to object_list or you can define your own variable to override it. we can override this by modifying PostListView as:
    context_object_name = 'posts'

    # defining the number of posts to show per page
    paginate_by = 5

    # now to get the post by onyl specific user we override get_query_set method as
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))  # here if the url has the argument username with value then we will get the object, if not then it will show the 404 not found error if user enters invalid author name
        return Post.objects.filter(author=user).order_by('-date_posted')   # order_by has to be here when we override the get_query_set method


class PostDetailView(DetailView):
    model = Post  # this is the only thing we need to do here. django sets all other necessary details needed
    
    # in detailview the default context_object_name is object but not object_list which is only for the listview



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # success_url='/'   # do this if you want to reddirect to the home page after successfully posting a new blog. but if rather want to redirect to the post-detail/post_id route then check models.py file

    # asigning the author to the currently logged in user by overriding the form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user # this basically is saying that the form that you are trying to submit, take it's instance and assign it's author to the current logged in user
        return super().form_valid(form)  # returing the form_valid method with the form argument which contains the author



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # asigning the author to the currently logged in user by overriding the form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

    # allowing the user to edit only his own post
    # this is a method that UserPassesTestMixin runs to check if the user passes certain test condition
    def test_func(self):
        post = self.get_object()  # gets the post that we are currently trying to update
        if self.request.user == post.author:  # ie checks if the current logged in user is the author of this post that he is trying to update
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # redirects to home page after successful deletion of the post

    # allowing the user to delete only his own post
    # this is a method that UserPassesTestMixin runs to check if the user passes certain test condition
    def test_func(self):
        post = self.get_object()  # gets the post that we are currently trying to delete
        if self.request.user == post.author:  # ie checks if the current logged in user is the author of this post that he is trying to update
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})