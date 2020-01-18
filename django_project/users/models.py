from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # PIL is pillow


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # extending the user field
    image= models.ImageField(default='default.jpg', upload_to='profile_pics')  # our own new custom field. here we are defining that the photos should be stored in profile_pics

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # for resizing the uploaded image
    # when we save our model then self is run by default here we are teying to override some of its functions
    def save(self):
        super().save()  # first we want to run the usual functionality of the profiles parent model's save method ie it saves the data

        img = Image.open(self.image.path)  # gets the path of the saved image

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # defining the size of the image to be used
            img.save(self.image.path)  # saves(ie overrides) the image in the same path

