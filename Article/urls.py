from django.conf.urls import url
from . import views

from django.conf.urls import url, include

app_name = 'Article'

urlpatterns = [
	url (r'^create/',views.CreateArticle,name="CreateArticle"),		
	url (r'^home/',views.home ,name="Home"),
	url (r'^(?P<pk>[0-9]+)/addLike/',views.AddLike ,name="AddLike"),
	      
	url (r'^(?P<pk>[0-9]+)/AddDislikeike/',views.AddDislike ,name="AddDislike")
]
