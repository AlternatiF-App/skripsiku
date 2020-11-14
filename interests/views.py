from django.shortcuts import render
from rest_framework import generics
from .serializers import *

class GetInterest(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
