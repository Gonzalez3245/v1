from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(null = True)
    #avatar

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    intro = models.TextField(null = True, blank = True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add= True, null= True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title




