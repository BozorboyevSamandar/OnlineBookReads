from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book


# Create your views here.

class BookListView(ListView):
    template_name = 'books/list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 2


# class BookListView(View):
#     def get(self, request):
#         books = Book.objects.all().order_by('id')
#         paginator = Paginator(books, 2)
#
#         page_num = request.GET.get('page', 1)
#         page_obj = paginator.get_page(page_num)
#
#         context = {'page_obj': page_obj}
#         return render(request, 'books/list.html', context)


class BookDetailView(DetailView):
    template_name = 'books/detail.html'
    pk_url_kwarg = 'id'
    model = Book

# class BookDetailView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         context = {'book': book}
#         return render(request, 'books/detail.html', context)
