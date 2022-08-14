from django.shortcuts import render
from django.db.models import Q
from blog.models import Blogpost

# Create your views here.


def blogView(req):
    # schools = data['schools']
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    blogposts = Blogpost.objects.filter(
        Q(title__icontains=query) | Q(subtitle__icontains=query))
    context = {
        "blog_page": "active",
        'blogposts': blogposts, 'title': 'blog'}
    return render(req, 'blog/index.html', context)
