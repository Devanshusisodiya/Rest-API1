from django.shortcuts import render
from .models import Hero
from .serializers import HeroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET'])
def getHerosAll(request):
    heros = Hero.objects.all()
    serializer = HeroSerializer(heros, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def postHero(request):
    serializer = HeroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    