from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name = 'blog-home'),# to be a home page left it as empty
    path('about/', views.about,name = 'blog-about'),
]
