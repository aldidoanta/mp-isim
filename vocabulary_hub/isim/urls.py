from django.urls import path
from django.views.generic import TemplateView
from isim import views

urlpatterns = [
    path('isim/', views.IsimList.as_view()),
    path('isim/<int:pk>/', views.IsimDetail.as_view()),
    path('isim/simulate', views.IsimSimulate.as_view()),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
