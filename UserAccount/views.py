from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from Article import views

# Create your views here.
def Login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'],password=request.POST['password'])
		if user is not None:
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST['next'])
			else:
				return render(request,'Article/CreateArticle.html')
		else:
			return render(request,'UserAccount/Signup.html',{'error':'User do not exist.'})
	else:
		return render(request,'UserAccount/loginPage.html')


def Logout(request):
	logout(request)
	return views.home(request)
	


def signup(request):
	if request.method == 'POST':
		try:
			user = User.objects.get(username=request.POST['username'])
			return render(request,'UserAccount/signup.html',{'error':'username already exists'})		
		except User.DoesNotExist:
			User.objects.create_user(request.POST['username'],email=request.POST['email'],password=request.POST['password'])
			return render(request,'UserAccount/loginPage.html')
	else:
   		return render(request,'UserAccount/signup.html')		