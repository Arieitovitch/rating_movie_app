from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('ratings', views.ratings, name='ratings'),
]