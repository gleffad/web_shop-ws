from django.urls import path
from tigAPI import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('product/<int:tigID>/', views.Product.as_view()),
    path('products/', views.ProductList.as_view()),
    path('productsGroup/', views.ProductGroup.as_view()),
    path('products/fish/', views.FishProductList.as_view()),
    path('products/shellfish/', views.ShellfishProductList.as_view()),
    path('products/seafood/', views.SeafoodProductList.as_view()),
    path('products/onsale/', views.OnSaleProductList.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transaction/<int:tigID>/', views.Transaction.as_view()),
    path('setdiscount/', views.SetDiscount.as_view()),
    path('decrementstock/', views.DecrementStock.as_view()),
    path('incrementstock/', views.IncrementStock.as_view()),
    path('comptability/', views.CustomComptability.as_view()),

    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
