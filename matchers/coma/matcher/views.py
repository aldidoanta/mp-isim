from rest_framework import generics, status
from rest_framework.response import Response
from matcher.models import Matcher
from matcher.serializers import MatcherSerializer


class MatcherGetMatches(generics.GenericAPIView):
    """
    Given a source schema and a target schema, returns the schema mapping as the output.
    """
    serializer_class = MatcherSerializer

    def post(self, request, format=None):
        serializer = MatcherSerializer(data=request.data)
        if serializer.is_valid():
            return Response(Matcher.get_matches(serializer.validated_data), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
