from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
#Data
posts = [
	{
		'author': 'Yassine',
		'title': 'Blog Post 1',
		'content': 'First Post Content',
		'date_posted': '06/07/2020'

	},
	{
		'author': 'Amine',
		'title': 'Blog Post 2',
		'content': 'Second Post Content',
		'date_posted': '07/07/2020'

	}

]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html',{'title': 'About'})
	#return HttpResponse('<h1>Blog About</h1> ')

