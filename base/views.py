from django.shortcuts import render
from django.db.models import Q

from blog.models import Blogpost
from .models import Demand, Offer
from schools.models import EduLevel, School


def home(req):
    # schools = data['schools']
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    edu_levels = EduLevel.objects.all()
    demands = Demand.objects.all()
    offers = Offer.objects.all()
    blogposts = Blogpost.objects.all()
    schools = School.objects.filter(
        Q(name__icontains=query) | Q(address__icontains=query))
    context = {
        "home_page": "active",
        'schools': schools,
        'edu_levels': edu_levels,
        'demands': demands,
        'offers': offers,
        'blogposts': blogposts,
        'title': 'schools'}
    return render(req, 'base/index.html', context)


def about(req):
    context = {
        "about_page": "active",
        "title": 'about'}
    return render(req, 'base/about.html', context)


def enquiries(req):
    context = {
        "enquiries_page": "active",
        "title": 'enquiries', }
    return render(req, 'base/enquiries.html', context)


def ccm(req):
    context = {
        "ccm_page": "active",
        "title": 'ccm', }
    return render(req, 'base/ccm.html', context)


def contact(req):
    context = {
        "contact_page": "active",
        "title": 'contact', }
    return render(req, 'base/contact.html', context)


def faq(req):
    context = {
        "faq_page": "active",
        "title": 'faq'}
    return render(req, 'base/faq.html', context)


def tariff(req):
    context = {
        "tariff_page": "active",
        "title": 'tariff'}
    return render(req, 'base/tariff.html', context)
