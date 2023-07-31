from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from matcher import views

urlpatterns = [
    path('matcher/get-matches', views.MatcherGetMatches.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
