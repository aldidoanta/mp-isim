from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from matcher.models import Matcher
from matcher.serializers import MatcherSerializer


class MatcherGetMatches(APIView):
    """
    Simulate an interoperability scenario, returning a schema mapping as the output
    """
    def post(self, request, format=None):
        serializer = MatcherSerializer(data=request.data)
        if serializer.is_valid():
            return Response(Matcher.get_matches(serializer.validated_data), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
