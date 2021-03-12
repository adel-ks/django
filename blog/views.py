from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
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
	if form.is_valid():
		# post is written to DB
		instance = form.save()
		print(instance)
		return HttpResponseRedirect('/blog/')

	context = {
	'form':form
	}
	return render(request, 'blog/create_post.html', context)


def update_post(request, post_id):
	# post = Post.objects.get(id = post_id)
	post = get_object_or_404(Post,id = post_id)
	# form = PostForm(request.POST or None, instance = post)
	form = PostForm(instance = post)
	if request.method == 'POST':
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blog/'+post_id +'/')
	context = {'form':form}
	return render (request, 'blog/update_post.html', context)


def delete_post(request, post_id):
	print(request)
	post = get_object_or_404(Post,id = post_id)
	if request.method == 'POST':
		post.delete()
		return HttpResponseRedirect('/blog/')

	context = {'post_id':post_id}
	return render(request, 'blog/delete_post.html', context)