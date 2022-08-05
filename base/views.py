from django.shortcuts import render
from django.db.models import Q
from schools.models import EduLevel, School


def home(req):
    # schools = data['schools']
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    edu_levels = EduLevel.objects.all()
    schools = School.objects.filter(
        Q(name__icontains=query) | Q(address__icontains=query))
    context = {'schools': schools,
               'edu_levels': edu_levels,  'title': 'schools'}
    return render(req, 'base/index.html', context)


def about(req):
    context = {"title": 'about'}
    return render(req, 'base/about.html', context)


def askList(req):
    context = {"title": 'ask-list', }
    return render(req, 'base/ask-list.html', context)


def ccm(req):
    context = {"title": 'ccm', }
    return render(req, 'base/ccm.html', context)


def contact(req):
    context = {"title": 'contact', }
    return render(req, 'base/contact.html', context)


def faq(req):
    context = {"title": 'faq'}
    return render(req, 'base/faq.html', context)
