from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response
from matcher.models import Matcher
from matcher.serializers import MatcherRequestSerializer, MatcherResponseSerializer


class MatcherGetMatches(generics.GenericAPIView):
    """
    Given a source schema and a target schema, returns the schema mapping as the output.
    """
    request_serializer_class = MatcherRequestSerializer

    @extend_schema(
        responses={201: MatcherResponseSerializer},
    )
    def post(self, request, format=None):
        request_serializer = self.request_serializer_class(data=request.data)
        if request_serializer.is_valid():
            matcher_results = Matcher.get_matches(request_serializer.validated_data)
            response_serializer = MatcherResponseSerializer(matcher_results, many=True)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
