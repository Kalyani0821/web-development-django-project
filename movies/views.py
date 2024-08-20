from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie


def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies.html', {'movies': data})

def home(request):
    return HttpResponse("Home Page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'details.html', {'movies': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'add.html')

def delete(request,id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    movie.delete()
    return HttpResponseRedirect('/movies')