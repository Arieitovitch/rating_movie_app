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
          username = request.POST['username']
          password = request.POST['password']
          username_lower = username.lower()
          password_lower = password.lower()
          user = authenticate(request, username=username_lower, password=password_lower)
          if user is not None:
               login(request, user)
               return redirect('home')
          else:
               message = 'Sorry, the username or password you have entered is invalid.'
               context = {
                    'message':message,
               }

               return render(request, 'rate/login.html', context)
     else:
          return render(request, 'rate/login.html')


def signup(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          confirm_password = request.POST['confirm_password']
          password_lower = password.lower()
          email = request.POST['Email']
          email_lower = email.lower()
          username_lower = username.lower()
          
          if confirm_password == password:

               if not User.objects.filter(username=username_lower).exists(): 
                    if not User.objects.filter(email=email_lower).exists():
                         User.objects.create_user(username=username_lower, password=password_lower, email=email_lower)
                         user = authenticate(username=username_lower, password=password_lower, email=email_lower)
                         login(request, user)
                         return redirect('home')
                    else: 
                         message = 'Sorry, That Email is taken'
                         context = {
                              'message':message,
                         }
                         return render(request, 'rate/signup.html', context)

               else: 
                    message = 'Sorry, That username is taken'
                    context = {
                         'message':message,
                    }
                    return render(request, 'rate/signup.html', context)
          else: 
               message = 'The passwords you have entered do not match'
               context = {
                    'message':message,
               }
               return render(request, 'rate/signup.html', context)
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
     ratings = Movie.objects.order_by('-score')

     context = {
          'Movie':ratings,
     }


          


     return render(request, 'rate/ratings.html', context)


