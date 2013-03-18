from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse
from django.template import RequestContext, Context, loader

def home(request):

    template = loader.get_template('home.html')
    dict = {"pagetitle": "Home",
            "page_template": 'base_page.html',
            }
    c = RequestContext(request, dict)
    return HttpResponse(template.render(c))
