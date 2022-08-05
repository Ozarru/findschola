from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from schools.models import School


class UserRole(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schools = models.ManyToManyField(School)

    def __str__(self):
        return self.name


class UserPost(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_added = models.DateTimeField(auto_now=True) # updates value at every update
    # date_added = models.DateTimeField(auto_now_add=True) # updates value only at creation

    def __str__(self):
        return self.name
