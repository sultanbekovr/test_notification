from rest_framework import serializers

from notification.models import Client, Order, Message


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class OrderReportSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class MessageReportSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class ReportSerializer(serializers.Serializer):
    order = serializers.IntegerField()
    status = serializers.BooleanField()
    count = serializers.IntegerField()

