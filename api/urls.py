from django.urls import path
# from .views import BookReviewDetailApiView, AllBookReviewAPIView
from rest_framework.routers import DefaultRouter
from .views import BookReviewViewSet

app_name = 'api'
route = DefaultRouter()
route.register("reviews", BookReviewViewSet, basename='review')
urlpatterns = route.urls

# urlpatterns = [
#     path('reviews/', AllBookReviewAPIView.as_view(), name='book-review-detail'),
#     path('reviews/<int:id>/', BookReviewDetailApiView.as_view(), name='review-list'),
#
# ]
# urlpatterns += route.urls
