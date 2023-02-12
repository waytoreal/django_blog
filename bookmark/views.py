from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

# Create your views here.
# BookmarkLV, BookmarkDV

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark