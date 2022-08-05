import json
from .models import *
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.views.generic import ListView, DetailView


# class SchoolListView(ListView):
#     model = School
#     context_object_name = 'schools'
#     template_name = 'schools/index.html'
#     ordering = ['date_added']


# class SchoolDetailView(DetailView):
#     model = School
#     # teachers = School.teacher_set.all()
#     template_name = 'schools/detail.html'


def schools(req):
    # data = whishlist(req)
    # wishes = data['wishes']

    # schools = School.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    schools = School.objects.filter(
        Q(name__icontains=query) | Q(address__icontains=query))
    edu_levels = EduLevel.objects.all()
    ordering = ['is_featured == True']
    context = {'schools': schools,
               'edu_levels': edu_levels,  'title': 'schools', 'ordering': ordering}

    return render(req, 'schools/index.html', context)


def school(req, slug):
    school = School.objects.get(slug=slug)
    # people
    teachers = school.teacher_set.all()
    # structures
    libraries = school.library_set.all()
    canteens = school.canteen_set.all()
    laboratories = school.laboratory_set.all()
    classrooms = school.classroom_set.all()
    # information
    reports = school.report_set.all()
    advantages = school.advantage_set.all()

    context = {'title': 'school',
               'school': school,
               'teachers': teachers,
               'classrooms': classrooms,
               'laboratories': laboratories,
               'libraries': libraries,
               'canteens': canteens,
               'reports': reports,
               'advantages': advantages
               }
    return render(req, 'schools/detail.html', context)


def allSchools(req):
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    schools = School.objects.filter(
        Q(name__icontains=query) | Q(address__icontains=query))
    edu_levels = EduLevel.objects.all()
    context = {'schools': schools,
               'edu_levels': edu_levels,  'title': 'all-schools'}

    return render(req, 'schools/all-schools.html', context)


def favs(req):
    # data = whishlist(req)
    # wishes = data['wishes']
    # order = data['order']
    # items = data['items']

    context = {
        # 'items': items, 'order': order, 'wishes': wishes,
        'title': 'favorites'
    }
    return render(req, 'schools/favs.html', context)
