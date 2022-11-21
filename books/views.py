from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Book


# Create your views here.


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'books/list.html', context)


class BookDetailView(DetailView):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {'book': book}
        return render(request, 'books/detail.html', context)
