from django.contrib import admin

from notification.models import OperatorCode, Tag, Client, Order, Message

admin.site.register([
    OperatorCode,
    Tag,
    Client,
    Order,
    Message
])
