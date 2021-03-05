from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
	context = {
	'variable': 'abc',
	'username': 'Adel',
	'my_friends':['Sasha','Gosha','Dima']
	}
	# return HttpResponse('<h1>Hello</h1>')
	return render(request, 'blog/index.html', context)


def post_list(request):
	get_posts = Post.objects.all()
	return render(request, "blog/posts_list.html",{'get_posts': get_posts})