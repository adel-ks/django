from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


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


def search_form(request):
	return render('search_form.html')


# def search(request):
# 	if 'q' in request.GET['q']:
# 		q = request.GET['q']
# 		posts = Post.objects.filter(title_icontains=q)
# 		return render('search_results.html', {'posts': posts, 'query':q})
# 	else:
# 		return render	 


def post_details(request, post_id):
	post = Post.objects.get(id = post_id)
	context = {
	'post': post
	}
	return render(request, 'blog/post_details.html', context)


def create_post(request):
	form = PostForm(request.POST or None)
