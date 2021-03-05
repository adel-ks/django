from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	# return HttpResponse('<h1>Hello</h1>')
	return render(request, 'blog/index.html')


def post_list(request):
	return render(request, "blog/posts_list.html")