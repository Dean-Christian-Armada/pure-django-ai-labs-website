from django.shortcuts import render

from . models import *

# Create your views here.
def index(request):
	template = 'blogs/index.html'
	items = Blog.objects.filter(published=True)
	context_dict = {}
	context_dict['items'] = items
	return render(request, template, context_dict)

def item(request, slug):
	template = 'blogs/item.html'
	item = Blog.objects.get(slug=slug)
	context_dict = {}
	context_dict['item'] = item
	return render(request, template, context_dict)