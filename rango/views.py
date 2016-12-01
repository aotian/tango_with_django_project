from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from rango.models import Category,Page


def index(request):
	category_list = Category.objects.order_by('-name')[:5]
	context_dict = {'categories':category_list}
	return render(request,'rango/index.html',context=context_dict)

def about(request):
	return render(request,'rango/about.html')

def show_category(request, category_name_slug):

	
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
	 	pages = Page.objects.filter(category=category)
	 	context_dict['pages'] = pages
	 	context_dict['category'] = category
	except Category.DoesNotExist, e:
		context_dict['category'] = None
	 	context_dict['pages'] = None
		raise e
	 	
	return render(request,'rango/category.html', context_dict)	
=======

def index(request):
	return HttpResponse("Rango says hey there partner!")
>>>>>>> 37371e080152e9541d80a9bf10ace4da61dff858
