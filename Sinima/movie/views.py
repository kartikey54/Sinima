from django.shortcuts import render
from .models import Movie
# Create your views here.
def index(request):
    all_movies = Movie.objects.all()
    movie_number = Movie.objects.count()
    context ={'all_movies' : all_movies,
              'movie_number' : movie_number,}
    return render(request, template_name='moviehome.html', context=context)