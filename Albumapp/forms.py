from django import forms
from django.core import validators
from .import models


class CreateAlbum(forms.ModelForm):
    class Meta:
        model = models.Albums
        fields = "__all__"