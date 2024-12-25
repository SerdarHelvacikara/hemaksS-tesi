from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ana sayfa
    path('products/', views.products, name="products"), # ürünler sayfası
    path('about/', views.about, name="about"),
    path('contact/', views.contacts, name = "contact"),
]