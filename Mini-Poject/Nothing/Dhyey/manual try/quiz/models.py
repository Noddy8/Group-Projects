from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=55, unique=True, null=True)
    profile_img = models.ImageField(upload_to='profile_images', default='user.png', blank=True, null=True, verbose_name='Profile pic')
    GENDER = (
        ('Male','Male'),
        ('female','Female'),
        ('Other','Other'),
    )
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)

    def __str__(self):
        return self.user.username

