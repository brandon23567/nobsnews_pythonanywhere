from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

def index(request):
	return render(request, "news/index.html")

############ index articles start #############

def article1(request):
	return render(request, "news/articles/article1.html")

def article2(request):
	return render(request, "news/articles/article2.html")

def article3(request):
	return render(request, "news/articles/article3.html")

############ index articles end ###############

def home(request):
	article = Article.objects.all().order_by('-date_posted')

	context = {
		'article': article
	}
	
	return render(request, "news/home.html", context)

def detail(request, pk):
	article = get_object_or_404(Article, id=pk)

	context = {
		'article':article
	}

	return render(request, "news/article_detail.html", context)


def signup(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {
		'form':form
	}

	return render(request, "news/signup.html", context)

def login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')


	return render(request, "news/login.html")