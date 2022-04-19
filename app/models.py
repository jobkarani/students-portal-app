from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_photo = CloudinaryField('image')
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return self.phone

    def __str__(self):
        return self.user.username