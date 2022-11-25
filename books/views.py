from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book, BookReview
from .forms import BookReviewForm


# Create your views here.

# class BookListView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = 'books'
#     paginate_by = 2


class BookListView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')

        search_query = request.GET.get('q', '')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 3)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'page_obj': page_obj,
            'search_query': search_query,
        }
        return render(request, 'books/list.html', context)


# class BookDetailView(DetailView):
#     template_name = 'books/detail.html'
#     pk_url_kwarg = 'id'
#     model = Book

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()

        context = {
            'book': book,
            'review_form': review_form,
        }
        return render(request, 'books/detail.html', context)


class AddReview(View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)
        context = {
            'book': book,
            'review_form': review_form,
        }
        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars=review_form.cleaned_data['stars'],
                comment=review_form.cleaned_data['comment'],
            )

            return redirect(reverse('books:detail', kwargs={"id": book.id}))

        return render(request, "books/detail.html", context)
