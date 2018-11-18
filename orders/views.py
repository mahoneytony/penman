# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Order
from .serializers import OrderSerializer, OrderUpdateSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = self.queryset
        order = get_object_or_404(queryset, number=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Order.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data,
                   status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


    def update(self, request, pk=None):
        serializer = OrderUpdateSerializer(data=request.data)
        if serializer.is_valid():
            order = self.queryset.filter(number=pk).update(**serializer.validated_data)
            return self.retrieve(request=request, pk=pk)
        else:
            return Response({'errors': serializer.errors})


    def partial_update(self, request, pk=None):
        pass
        #return Response({'asdasd': request.method})