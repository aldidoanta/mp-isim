from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from isim.models import Isim
from isim.serializers import IsimSerializer


class IsimSimulate(APIView):
    """
    Simulate an interoperability scenario, returning a schema mapping as the output
    """
    def post(self, request, format=None):
        serializer = IsimSerializer(data=request.data)
        if serializer.is_valid():
            return Response(Isim.simulate(serializer.validated_data), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IsimList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    List all interoperability scenarios, or create a new one.
    """
    queryset = Isim.objects.all()
    serializer_class = IsimSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class IsimDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    """
    Retrieve, update, or delete an interoperability scenario.
    """
    queryset = Isim.objects.all()
    serializer_class = IsimSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
