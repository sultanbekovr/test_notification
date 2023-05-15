from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            interval = IntervalSchedule.objects.create(every=10, period=IntervalSchedule.SECONDS)
            PeriodicTask.objects.create(name='auto_send_message', interval=interval, task='notification.tasks.send_message')
            print('Создана задача с периодичность 10 секунд')
        except Exception as e:
            print("Не удалось создать периодичную задачу")
            print(e)