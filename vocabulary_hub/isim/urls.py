from django.urls import path
from isim import views

urlpatterns = [
    path('isim/', views.isim_list),
    path('isim/<int:pk>/', views.isim_detail),
]
