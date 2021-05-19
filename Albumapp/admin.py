from django.contrib import admin
from .models import Albums, Images
# Register your models here.

class AlbumsAdmin(admin.ModelAdmin):

    list_display = [
        'thumbnail',
        'title',
        'discription',
        'creation'
    ]

admin.site.register(Albums, AlbumsAdmin)


class ImagesAdmin(admin.ModelAdmin):

    list_display = [
        'thumbnail',
        'discription',
        'creation'
    ]

admin.site.register(Images, ImagesAdmin)

