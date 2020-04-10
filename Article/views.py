from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.utils import timezone
from django.db import models
from django.contrib.auth.decorators import login_required
from Article.models import Posts



# Create your views here.

@login_required(login_url='/Login/Login/')
def CreateArticle(request):
	if request.method == 'POST':

		p = Posts(post_text=request.POST['postText'], pub_date=timezone.datetime.now(), user= request.user)
		p.save()
	#	ShowArticles(request)
		return redirect('home')
	else:
		return render(request, 'Article/CreateArticle.html')
'''
def ShowArticles(request):
	data = Posts.objects.order_by('pub_date')
	print(data.contribunt())

	#for posttext in data:
	#	print(posttext)
	return render(request,"Home/Home.html",  {'posts':data})
'''

def home(request):
    posts = Posts.objects.order_by('pub_date')

    #print (post)
    return render(request, 'Article/Home.html', {'posts':posts})

def AddLike(request,pk):
	p = Posts.objects.get(id=pk)
	p.likes += 1
	p.save()
	return home(request)

def AddDislike(request,pk):
	p = Posts.objects.get(id=pk)
	p.dislikes += 1
	p.save()
	return home(request)