from django.urls import path
from .migrations import views

urlpatterns = [
    path('', views.all_products, name='products')
]
