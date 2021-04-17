from django.urls import path
from tigAPI import views

urlpatterns = [
    path('products/', views.ProductsDetailsList.as_view()),
    path('product/<int:tigID>/', views.ProductDetails.as_view()),
    path('transaction/', views.ProductsDetailsList.as_view()),
    path('transaction/<int:tigID>/', views.ProductDetails.as_view()),
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
    path('infoproduct/<int:pk>/', views.DetailsInfoProduct.as_view()),
    path('infoproducts/', views.InfoProducts.as_view()),
    path('putonsale/<int:pk>/<str:newprice>/', views.PutOnSale.as_view()),
    path('removesale/<int:pk>/', views.Removesale.as_view()),
    path('incrementStock/<int:pk>/<int:number>/',
         views.IncrementStock.as_view()),
    path('decrementStock/<int:pk>/<int:number>/',
         views.DecrementStock.as_view()),
]
