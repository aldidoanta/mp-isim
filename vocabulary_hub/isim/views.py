from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from isim.models import Isim
from isim.serializers import IsimSerializer


@csrf_exempt
def isim_list(request):
    """
    List all interoperability scenarios, or create a new one.
    """
    if request.method == 'GET':
        isim = Isim.objects.all()
        serializer = IsimSerializer(isim, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IsimSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def isim_detail(request, pk):
    """
    Retrieve, update, or delete an interoperability scenario.
    """
    try:
        isim = Isim.objects.get(pk=pk)
    except Isim.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IsimSerializer(isim)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IsimSerializer(isim, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        isim.delete()
        return HttpResponse(status=204)
