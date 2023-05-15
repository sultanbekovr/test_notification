import pytz
from django.db import models


class OperatorCode(models.Model):
    """ Код мобильного оператора """
    code = models.CharField('Код мобильного оператора', max_length=5)

    class Meta:
        db_table = 'operator_code'


class Tag(models.Model):
    """ Тэги пользователей """
    tag = models.CharField('Тэг пользователя', max_length=255)

    class Meta:
        db_table = 'tag'


class Client(models.Model):
    """ Клиент для рассылки """
    phone_number = models.CharField('Номер телефона', max_length=11)
    operator_code = models.CharField('Код оператор')
    tag = models.CharField('Тэг', max_length=100)
    timezone = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    class Meta:
        db_table = 'client'


class Order(models.Model):
    """ Рассылки """
    start_datetime = models.DateTimeField('Дата начала рассылки')
    end_datetime = models.DateTimeField('Дата окончания рассылки')
    text = models.TextField('Текст сообщения')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True)
    operator_code = models.ForeignKey(OperatorCode, on_delete=models.CASCADE, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'order'


class Message(models.Model):
    """ Созданные сообщения """
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.BooleanField('Cтатус отправки', default=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'message'




