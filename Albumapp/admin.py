from django.contrib import admin
from .models import Albums
# Register your models here.

class AlbumsAdmin(admin.ModelAdmin):

    list_display = [
        'thumbnail',
        'title',
        'discription',
        'creation'
    ]

admin.site.register(Albums, AlbumsAdmin)

