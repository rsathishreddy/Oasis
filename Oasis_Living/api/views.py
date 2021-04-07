from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

from rest_framework.parsers import JSONParser

from .models import Candidate

from .serializers import CandidateSerializer

# Create your views here.


def candidateView(request):
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
