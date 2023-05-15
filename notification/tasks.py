import os
from datetime import datetime

import pytz
import requests

from django.db.models import Q
from django.core.mail import send_mail

from config.celery_app import app
from config.settings import env
from notification.models import Order, Client, Message


@app.task
def send_message():
    orders = Order.objects.filter(Q(end_datetime__gt=datetime.now()) &
                                  Q(start_datetime__lte=datetime.now()) &
                                  Q(status=True))
    token = env('NOTIFICATION_TOKEN')
    headers = {
        'Authorization': f'Bearer {token}'
    }

    for order in orders:
        order.status = False
        order.save()
        clients = Client.objects.filter(Q(tag=order.tag.tag) & Q(operator_code=order.operator_code.code))
        if order.end_datetime.replace(tzinfo=pytz.timezone("UTC")) > datetime.now().replace(tzinfo=pytz.timezone("UTC")):
            for client in clients:
                message = Message.objects.create(order=order, client=client)
                url = f"https://probe.fbrq.cloud/v1/send/{message.id}/"
                payload = {
                    'id': message.id,
                    'text': order.text,
                    'phone': client.phone_number
                }
                try:
                    requests.request("POST", url, headers=headers, data=payload)
                except requests.RequestException:
                    message.status = False

                message.save()