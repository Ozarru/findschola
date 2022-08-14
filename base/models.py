from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import CustomUser
# from schools.models import School


class Demand(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # updates value only at creation
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # updates value only at creation
    date_added = models.DateTimeField(auto_now_add=True)
    # date_added = models.DateTimeField(auto_now=True) # updates value at every update

    def __str__(self):
        return self.name
