from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.models import ProductModel, CategoryModel, ReviewModel
from product.serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer


class ProductsListAPIView(ListCreateAPIView):
	queryset = ProductModel.objects.all()
	serializer_class = ProductListSerializer


class ProductsDetailAPIView(RetrieveUpdateDestroyAPIView):
	queryset = ProductModel.objects.all()
	serializer_class = ProductListSerializer
	lookup_field = 'id'



class CategoriesListAPIView(ListCreateAPIView):
	queryset = CategoryModel.objects.all()
	serializer_class = CategoryListSerializer


class CategoriesDetailAPIView(RetrieveUpdateDestroyAPIView):
	queryset = CategoryModel.objects.all()
	serializer_class = CategoryListSerializer
	lookup_field = 'id'



class ReviewsListAPIView(ListCreateAPIView):
	queryset = ReviewModel.objects.all()
	serializer_class = ReviewListSerializer


class ReviewsDetailAPIView(RetrieveUpdateDestroyAPIView):
	queryset = ReviewModel.objects.all()
	serializer_class = ReviewListSerializer
	lookup_field = 'id'
