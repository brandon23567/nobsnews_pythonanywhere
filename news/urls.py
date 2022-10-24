from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('home/', views.home, name="home"),

	path('signup/', views.signup, name="signup"),
	path('login/', views.login, name="login"),

	########### index articles urls start #############
	path('article1/', views.article1, name="article1"),
	path('article2/', views.article2, name="article2"),
	path('article3/', views.article3, name="article3"),
	########### index articles urls end ###############

	path('<int:pk>/', views.detail, name="detail"),

]