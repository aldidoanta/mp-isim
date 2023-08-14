from django.urls import path
from isim import views

urlpatterns = [
    path('isim/', views.IsimList.as_view()),
    path('isim/<int:pk>/', views.IsimDetail.as_view()),
    path('isim/simulate', views.IsimSimulate.as_view()),
]
