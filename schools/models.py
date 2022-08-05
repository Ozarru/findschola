from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class EduLevel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(default='example@school.com', null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    address = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=255, default='00-00-00-00')
    cel = models.CharField(max_length=255, default='00-00-00-00')
    moto = models.CharField(max_length=255, default='slogan')
    year_founded = models.CharField(max_length=4, null=True)
    mgt_quote = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ad_copy = models.TextField(blank=True, null=True)
    resumption = models.CharField(max_length=180, default='', null=True)
    # academia
    availability = models.TextField(blank=True, null=True)
    pedagogy = models.TextField(blank=True, null=True)
    awards = models.CharField(max_length=255, default='')
    diplomas = models.CharField(max_length=255, default='', null=True)
    courses = models.CharField(max_length=255, default='', null=True)
    time_range = models.CharField(max_length=255, default='', null=True)
    price_range = models.CharField(max_length=255, default='', null=True)
    edu_levels = models.ManyToManyField(EduLevel)
    staff = models.IntegerField(default='0', null=True)
    students = models.IntegerField(default='0', null=True)
    curriculums = models.IntegerField(default='0', null=True)
    success_rate = models.IntegerField(default='0', null=True)

    # structures
    classes = models.IntegerField(default='0', null=True)
    labs = models.IntegerField(default='0', null=True)
    libs = models.IntegerField(default='0', null=True)
    canteens = models.IntegerField(default='0', null=True)
    faculties = models.IntegerField(default='0', null=True)
    # profile
    is_featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        upload_to='schools/thumbnails', blank=True, null=True)
    banner = models.ImageField(
        upload_to='schools/banners', blank=True, null=True)
    crest = models.ImageField(
        upload_to='schools/crests', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.area, self.title)
        super(School, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school-detail', kwargs={'slug': self.slug})


class Photo(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/photos', blank=True, null=True)


class Stat(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    year = models.CharField(max_length=4, default='year')
    pass_rate = models.IntegerField(default='0')
    fail_rate = models.IntegerField(default='0')


class Teacher(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    xp = models.IntegerField(default='0')
    fullname = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    qualifications = models.CharField(max_length=255, null=True)
    image = models.ImageField(
        upload_to='schools/teachers', blank=True, null=True)
    facebook = models.CharField(
        max_length=255, default='', null=True, blank=True)
    twitter = models.CharField(
        max_length=255, default='', null=True, blank=True)
    instagram = models.CharField(
        max_length=255, default='', null=True, blank=True)
    linkedin = models.CharField(
        max_length=255, default='', null=True, blank=True)


class Advantage(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    phrase = models.CharField(max_length=255, default='avantage',)


class Classroom(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/classrooms', blank=True, null=True)
    label = models.CharField(max_length=255, default='image label')
    info = models.TextField(blank=True, null=True)


class Laboratory(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/laboratories', blank=True, null=True)
    label = models.CharField(max_length=255, default='image label')
    info = models.TextField(blank=True, null=True)


class Library(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/libraries', blank=True, null=True)
    label = models.CharField(max_length=255, default='image label')
    info = models.TextField(blank=True, null=True)


class Canteen(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/canteens', blank=True, null=True)
    label = models.CharField(max_length=255, default='image label')
    info = models.TextField(blank=True, null=True)


class Report(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/reports', blank=True, null=True)
    title = models.CharField(max_length=255, default='News Title')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, default='News')
    date_posted = models.DateTimeField(auto_now=True)
