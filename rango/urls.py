from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
<<<<<<< HEAD
	url(r'^about/$',views.about,name='about'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
		views.show_category, name='show_category'),
=======
>>>>>>> 37371e080152e9541d80a9bf10ace4da61dff858
]