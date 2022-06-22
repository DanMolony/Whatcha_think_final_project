from django.shortcuts import render
from django.contrib.auth.models import User
from .models import FilmPoster
# Create your views here.
class FilmPostView(User,FilmPoster):
    model = FilmPoster
    
    def upload(request):
        if request.method == 'POST':
            form = FilmPoster(request.POST)
        if form.is_valid():
            form.save