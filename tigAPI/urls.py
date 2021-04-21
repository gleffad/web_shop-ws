from django.urls import path
from tigAPI import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/fish', views.ProductFish.as_view()),
    path('products/shellfish', views.ProductShellfish.as_view()),
    path('products/seafood', views.ProductSeafood.as_view()),
    path('product/<int:tigID>/', views.Product.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transaction/<int:tigID>/', views.Transaction.as_view()),
    path('setdiscount/<int:tigID>/<int:discount>/', views.SetDiscount.as_view()),
    path('decrementstock/<int:tigID>/<int:qty>/<int:operation>/',
         views.DecrementStock.as_view()),
    path('incrementstock/<int:tigID>/<int:qty>/',
         views.IncrementStock.as_view()),
    path('onsaleproducts/', views.OnSaleProductList.as_view())
]
'''
    path('<str:product_type>/comptability/<str:time_format>>', views.CustomComptability.as_view()),
    path('comptability/<str:time_format>>', views.Comptability.as_view()),
'''
