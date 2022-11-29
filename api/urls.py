from django.urls import path
from .views import BookReviewDetailApiView, AllBookReviewAPIView


urlpatterns = [
    path('reviews/', AllBookReviewAPIView.as_view(), name='book-review-detail'),
    path('reviews/<int:id>/', BookReviewDetailApiView.as_view(), name='review-list'),

]