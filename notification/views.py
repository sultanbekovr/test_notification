import json

from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notification.models import Client, Order, Message, Tag, OperatorCode
from notification.serializers import ClientSerializer, OrderSerializer, MessageReportSerializer, ReportSerializer


class ListCreateClient(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        Tag.objects.get_or_create(tag=request.data.get('tag'))
        OperatorCode.objects.get_or_create(code=request.data.get('operator_code'))

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RetrieveUpdateDestroyClient(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ListCreateOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class RetrieveUpdateDestroyMessage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageReportSerializer


@api_view(('GET',))
def consolidated_report(request):
    messages = Message.objects.all().values('order', 'status').annotate(count=Count('pk'))
    serializer = ReportSerializer(messages)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('GET',))
def retrieve_report(request, pk):
    messages = Message.objects.filter(order_id=pk)
    serializer = MessageReportSerializer(messages, many=True)

    return Response(serializer.data)
