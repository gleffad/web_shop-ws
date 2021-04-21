from django.urls import path
from tigAPI import views

urlpatterns = [
    path('product/<int:tigID>/', views.Product.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/fish', views.FishProductList.as_view()),
    path('products/shellfish', views.ShellfishProductList.as_view()),
    path('products/seafood', views.SeafoodProductList.as_view()),
    path('products/onsale', views.OnSaleProductList.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transaction/<int:tigID>/', views.Transaction.as_view()),
    path('setdiscount/', views.SetDiscount.as_view()),
    path('decrementstock/<int:tigID>/<int:qty>/<int:operation>/',
         views.DecrementStock.as_view()),
    path('incrementstock/', views.IncrementStock.as_view())
]
'''
    path('<str:product_type>/comptability/<str:time_format>>', views.CustomComptability.as_view()),
    path('comptability/<str:time_format>>', views.Comptability.as_view()),
'''
