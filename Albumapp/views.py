from django.shortcuts import render
from .models import Albums, Images
# Create your views here.

def albumspage(request):
    albums = Albums.objects.all()
    context = {
        'albums':albums

    }
    return render(request, 'album/albums.html', context)


def view_photo(request):
    images = Images.objects.all()

    context = {
        'images':images
    }
    return render(request, 'album/view_photo.html', context)


def view_all_photo(request):

    context = {
    }
    return render(request, 'album/view_all_photo.html', context)


def edit_album(request):

    context = {

    }
    return render(request, 'album/edit_album.html', context)