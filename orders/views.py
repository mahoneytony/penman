# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def create(self, request, *args, **kwarg):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         Order.objects.create(serializer.validated_data)
    #         return Response(serializer.validated_data,
    #                status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors)

    # def perform_create(self, serializer):
    #    serializer.save()
