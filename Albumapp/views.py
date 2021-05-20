from django.shortcuts import render
from .models import Albums, Images
from Albumapp import forms
# Create your views here.


def create_album(request):
    create_form = forms.CreateAlbum()

    if request.method == 'POST':

        create_form = forms.CreateAlbum(request.POST)

        if create_form.is_valid():
            create_form.save(commit = True)
            return albumspage(request)


    dict = {
        'massage':'success',
        'create_form':create_form
    }

    return render(request, 'album/forms.html', context=dict)


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