from django.urls import path
from tigAPI import views

urlpatterns = [
    path('products/', views.ProductsDetailsList.as_view()),
    path('product/<int:TigID>/', views.ProductDetails.as_view()),
    path('transactions/', views.ProductsDetailsList.as_view()),
    path('transaction/<int:TigID>/', views.ProductDetails.as_view()),
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:TigID>/', views.PromoDetail.as_view()),
    path('infoproduct/<int:TigID>/', views.DetailsInfoProduct.as_view()),
    path('infoproducts/', views.InfoProducts.as_view()),
    path('putonsale/<int:TigID>/<str:newprice>/', views.PutOnSale.as_view()),
    path('removesale/<int:TigID>/', views.Removesale.as_view()),
    path('incrementStock/<int:TigID>/<int:number>/',
         views.IncrementStock.as_view()),
    path('decrementStock/<int:TigID>/<int:number>/',
         views.DecrementStock.as_view()),
    path('productsbycategory/<int:category>/', views.ProductsListPerType.as_view()),
]