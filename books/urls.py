from django.urls import path
from .views import BookListView, BookDetailView, AddReview, EditReview, ConfirmDeleteReview, DeleteReview

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:id>/', BookDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddReview.as_view(), name='review'),
    path('<int:book_id>/reviews/<int:review_id>/edit', EditReview.as_view(), name='edit-review'),
    path('<int:book_id>/reviews/<int:review_id>/delete/confirm', ConfirmDeleteReview.as_view(), name='confirm-delete-review'),
    path('<int:book_id>/reviews/<int:review_id>/delete', DeleteReview.as_view(), name='delete-review'),
]
