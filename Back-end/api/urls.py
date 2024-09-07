from django.urls import path
from userauths import views as userauths_views
from store import views as store_views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [

    path('user/token/' , userauths_views.MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('user/token/refresh/' , TokenRefreshView.as_view(),name='token_refresh'),
    path('user/register/', userauths_views.RegisterView.as_view(),name='auth_register'),
    path('category/',store_views.CategoryListView.as_view()),
    path('products/',store_views.ProductListView.as_view()),
    path('products/<int:pk>/',store_views.ProductDetailAPIView.as_view()),
    path('products/<slug:slug>/', store_views.ProductDetailAPIView.as_view()),
    path('cart-view/', store_views.CartAPIView.as_view()),

]
