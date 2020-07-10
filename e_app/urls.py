from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name="home"),
        path('cart', views.cart, name="cart"),
        path('checkout', views.checkout, name="checkout"),
        path('home', views.home, name="home"),
        path('update_item/', views.updateItem, name="update_item"),
        path('process_order/', views.processOrder, name="process_order"),

]
