from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()  # unlike charfield this takes unlimited input character
    date_posted=models.DateTimeField(default=timezone.now) # gives the data at which the post is actually created ie after updating the post the dateposted field is not updated
    author=models.ForeignKey(User, on_delete=models.CASCADE) # to join two tables user foreignkey. here on_dlete means delete the post when the user is delected

    def __str__(self):
        return self.title   # this tells to show the post table's content as post's title in shell

    # here we will redirect them to the post-detail page. to do this we don't use redirect function(which actually redirects you to the specific route) but will use reverse function (which return the full url as a string to that route) and let the view handle the redirect for us which is done by createview.
    # we will create a get_absolute_url method to tell django how to find specific url to any instance of a post
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk}) # post-detail is the route and pk is the primary key ie id of the id to show detail of
        

    

