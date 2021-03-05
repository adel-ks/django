from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	context = {
	'variable': 'abc'
	}
	# return HttpResponse('<h1>Hello</h1>')
	return render(request, 'blog/index.html', context)


def post_list(request):
	return render(request, "blog/posts_list.html")