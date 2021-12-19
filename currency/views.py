from django.shortcuts import render
from currency.models import History
from currency.serializers import  HistorySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
# Create your views here.
@csrf_exempt
def currency_list(request):
    """
    List all code currency history list, or create a new currency.
    """
    if request.method == 'GET':
        source = request.GET.get("s", 404)
        if source == 404:
            return JsonResponse({"error": 1, "message": "Source currency not provided."})
        histories = History.objects.all()
        serializer = HistorySerializer(histories, many=True)
        return JsonResponse(serializer.data, safe=False)

    
@csrf_exempt
def create_history(request):
    if request.method == 'POST':
        print(request)
        data = JSONParser().parse(request)
        serializer = HistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=405)

    else:
        return JsonResponse({"error": 1, "message": "Bad Request"}, status=405)
