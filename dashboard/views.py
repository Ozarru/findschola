import json
from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# from .forms import SchoolForm


@login_required(login_url='login')
def dashboard(req):
    context = {
        "dash_page": "active", "title": 'dashboard'}
    return render(req, 'dashboard/index.html', context)


@login_required(login_url='login')
def profile(req):
    context = {
        "profile_page": "active", "title": 'profile'}
    return render(req, 'dashboard/profile.html', context)


@login_required(login_url='login')
def settings(req):
    context = {
        "settings_page": "active", "title": 'settings'}
    return render(req, 'dashboard/settings.html', context)


@login_required(login_url='login')
def comms(req):
    context = {
        "comms_page": "active", "title": 'comms'}
    return render(req, 'dashboard/comms.html', context)


@login_required(login_url='login')
def notices(req):
    context = {
        "notices_page": "active", "title": 'notices'}
    return render(req, 'dashboard/notices.html', context)


@login_required(login_url='login')
def bulletin(req):
    context = {
        "bulletin_page": "active", "title": 'bulletin'}
    return render(req, 'dashboard/bulletin.html', context)


@login_required(login_url='login')
def plans(req):
    context = {
        "plans_page": "active", "title": 'plans'}
    return render(req, 'dashboard/plans.html', context)
