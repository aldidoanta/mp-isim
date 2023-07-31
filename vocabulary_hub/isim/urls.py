from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from isim import views

urlpatterns = [
    path('isim/', views.IsimList.as_view()),
    path('isim/<int:pk>/', views.IsimDetail.as_view()),
    path('isim/simulate', views.IsimSimulate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
