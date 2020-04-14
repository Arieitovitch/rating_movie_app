from django.shortcuts import render, redirect

from . models import Movie, User
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from . movies_id import get_Movie
from decimal import * 
# Create your views here.




def signin(request):
     if request.user.is_authenticated:
          return redirect('home')
     if request.method == 'POST':
          print (request)
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request, user)
               return redirect('home')
          else:
               return render(request, 'rate/login.html')
     else:
          return render(request, 'rate/login.html')


def signup(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          email = request.POST['Email']
          User.objects.create_user(username=username, password=password, email=email)
          user = authenticate(username=username, password=password, email=email)
          login(request, user)
          return redirect('home')
     else:
          return render(request, 'rate/signup.html',)

def home(request): 

     movie = get_Movie()
     title = movie.title
     genre = movie.genre
     image = movie.image
     director = movie.director
     actors = movie.actors

     if not Movie.objects.filter(title=title).exists():
          Movie.objects.create(title=title, image=image, actors=actors, genre=genre, director=director)

     film =  {
          'film':Movie.objects.get(title=title)
     } 



     if request.method == 'GET' and not request.user.is_authenticated:
          return redirect('signin')

     if request.method == 'POST' and request.POST.get('logout') == 'logout':
          logout(request)
          return redirect('signin')

     if request.method == 'POST':

          if request.POST.get('like') == 'like':
               new = request.POST['new']
               var = Movie.objects.get(title=new)
               print(var.vote, title)
               var.vote += 1
               var.like += 1
               var.save()

          elif request.POST.get('dislike') == 'dislike':
               new = request.POST['new']
               var = Movie.objects.get(title=new)
               var.vote += 1
               var.dislike += 1
               var.save() 



     return render(request, 'rate/home.html', film)

def rate_movies():
     movies_all = Movie.objects.all()

     for M in movies_all:
          if M.vote != 0:
               v = Decimal(M.vote)
               l = Decimal(M.like)
               d = Decimal(M.dislike)
               s = Decimal((l - d)/v)
               s_str = str(s)
               M.score = s_str
               M.save()


def ratings(request):
     movie_object = Movie.objects.all()

     rate_movies()
     ratings = reversed(Movie.objects.order_by('score'))
     context = {
          'Movie':ratings,
     }


          


     return render(request, 'rate/ratings.html', context)


