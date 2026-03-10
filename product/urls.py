from django.urls import path
from .views import (
    ProductsListAPIView, ProductsDetailAPIView,
    CategoriesListAPIView, CategoriesDetailAPIView,
    ReviewsListAPIView, ReviewsDetailAPIView
)

urlpatterns = [
    path('products/', ProductsListAPIView.as_view()),
    path('products/<int:product_id>/', ProductsDetailAPIView.as_view()),

    path('categories/', CategoriesListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoriesDetailAPIView.as_view()),

    path('reviews/', ReviewsListAPIView.as_view()),
    path('products/<int:product_id>/reviews/', ReviewsListAPIView.as_view()),
    path('reviews/<int:review_id>/', ReviewsDetailAPIView.as_view()),
]