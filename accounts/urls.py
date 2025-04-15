from django.urls import path
from . import views

urlpatterns = [
    ## ACOOUNT URLS
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),  # Register page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),
    path('shop/', views.shop, name='shop'),  
  
  ## CART URLS
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('shop-cart/', views.shop_cart, name='shop-cart'),
    path('delete_cart_item/<int:product_id>/', views.delete_cart_item, name='delete_cart_item'),

## CHECKOUT/ ORDER
   
    path('checkout/', views.checkout_view, name='checkout'),
    path('submit-address/', views.submit_address_view, name='submit_address'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),

    path('button-works/', views.button_works, name='button_works'),


]