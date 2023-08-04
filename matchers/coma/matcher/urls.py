from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from matcher import views

urlpatterns = [
    path('matcher/get-matches', views.MatcherGetMatches.as_view()),
    # path to the OpenAPI dynamic schema
    path('schema', get_schema_view(
        title="Matcher - COMA",
        description="API endpoints of COMA Matcher",
        version="1.0.0"
    ), name='openapi-schema'),
    # path to the generated OpenAPI docs using Swagger UI
    path('api', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
