from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Server, Metric
from .serializers import ServerSerializer, MetricSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all().order_by('-timestamp')
    serializer_class = MetricSerializer