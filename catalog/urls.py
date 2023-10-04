from django.urls import path
from . import views
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)

urlpatterns = [
    path('products/<int:product_id>/', views.show_product, name='show_product'),
    path('', BlogPostListView.as_view(), name='blogpost-list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('create/', BlogPostCreateView.as_view(), name='blogpost-create'),
    path('<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost-delete'),
]