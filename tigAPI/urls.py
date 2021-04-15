from django.urls import path
from tigAPI import views

urlpatterns = [
    path('products/', views.ProductsDetailsList.as_view()),
    path('product/<int:tigID>/', views.ProductDetails.as_view()),
]