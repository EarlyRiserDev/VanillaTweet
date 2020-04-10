from django.conf.urls import url
from . import views

from django.conf.urls import url, include

app_name = 'UserAccount'

urlpatterns = [
	url (r'^Login/',views.Login,name="Login"),
	url (r'^Logout/',views.Logout,name="Logout"),
	url (r'^signup/',views.signup,name="signup"),
	

]
