from django.core.management.base import BaseCommand
from myapp.models import Worker, Store

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        worker = Worker.objects.create(name='John Doe', phone_number='1234567890')
        Store.objects.create(name='Store 1', worker=worker)
        Store.objects.create(name='Store 2', worker=worker)