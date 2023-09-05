from django.urls import path
from django.views.generic import TemplateView
from matcher import views

urlpatterns = [
    path('matcher/match-schemas', views.MatcherMatchSchemas.as_view()),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
