from django.urls import path
from .views import ProductListCreateView

urlpatterns = [
    path('films/', ProductListCreateView.as_view(), name='film-list-create'),
]
