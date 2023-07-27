from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from isim.models import Isim
from isim.serializers import IsimSerializer


@api_view(['GET', 'POST'])
def isim_list(request, format=None):
    """
    List all interoperability scenarios, or create a new one.
    """
    if request.method == 'GET':
        isim = Isim.objects.all()
        serializer = IsimSerializer(isim, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IsimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def isim_detail(request, pk, format=None):
    """
    Retrieve, update, or delete an interoperability scenario.
    """
    try:
        isim = Isim.objects.get(pk=pk)
    except Isim.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IsimSerializer(isim)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IsimSerializer(isim, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        isim.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
