from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .pagination import *

class GetInterest(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    pagination_class = StandardResultsSetPagination
