from django.shortcuts import render
from django import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage
# Create your views here.

def search(request):
    query = request.GET['q']
    results = FlatPage.objects.filter(content__icontains=query)
    template = loader.get_template('search/search.html')
    context = Context({ 'query': query, 'results': results })
    response = template.render(context)
    return HttpResponse(response)

