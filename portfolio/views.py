from django.shortcuts import render
from .content import SITE_CONTENT


def base_context(active='home'):
    return {'content': SITE_CONTENT, 'active': active}


def home(request):
    return render(request, 'portfolio/home.html', base_context('home'))


def resume(request):
    return render(request, 'portfolio/resume.html', base_context('resume'))


def projects(request):
    return render(request, 'portfolio/projects.html', base_context('projects'))


def contact(request):
    sent = request.method == 'POST'
    return render(request, 'portfolio/contact.html', {**base_context('contact'), 'sent': sent})
