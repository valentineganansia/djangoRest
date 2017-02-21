from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Items
from .serializers import ItemsSerializer

def index(request):
    return HttpResponse("Hello, welcome to myshop")
# Create your views here.

class ItemsViewSet(viewsets.ModelViewset):
    queryset=Items.objects.all()
    serializer_class=ItemsSerializer