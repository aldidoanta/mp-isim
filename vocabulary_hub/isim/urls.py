from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from isim import views

urlpatterns = [
    path('isim/', views.isim_list),
    path('isim/<int:pk>/', views.isim_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
