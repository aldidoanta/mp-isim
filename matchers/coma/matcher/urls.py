from django.urls import path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from matcher import views

urlpatterns = [
    path('matcher/get-matches', views.MatcherGetMatches.as_view()),
    # path to the OpenAPI dynamic schema
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path to the generated OpenAPI docs using Swagger UI
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
