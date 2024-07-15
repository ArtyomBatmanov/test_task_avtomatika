from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Worker, Store, Visit
from django.utils import timezone

class StoreListView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Phone '):
            return Response({'error': 'Authorization header missing or incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        phone_number = auth_header.split(' ')[1]
        worker = get_object_or_404(Worker, phone_number=phone_number)
        stores = Store.objects.filter(worker=worker)
        if not stores:
            return Response({'error': 'No stores found for this worker'}, status=status.HTTP_404_NOT_FOUND)

        stores_data = [{'pk': store.pk, 'name': store.name} for store in stores]
        return Response(stores_data, status=status.HTTP_200_OK)

class VisitCreateView(APIView):
    def post(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Phone '):
            return Response({'error': 'Authorization header missing or incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        phone_number = auth_header.split(' ')[1]
        worker = get_object_or_404(Worker, phone_number=phone_number)
        store_id = request.data.get('store_id')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        if not store_id or latitude is None or longitude is None:
            return Response({'error': 'store_id, latitude, and longitude are required'}, status=status.HTTP_400_BAD_REQUEST)

        store = get_object_or_404(Store, pk=store_id, worker=worker)
        visit = Visit.objects.create(
            worker=worker,
            store=store,
            latitude=latitude,
            longitude=longitude,
            datetime=timezone.now()
        )

        visit_data = {
            'pk': visit.pk,
            'datetime': visit.datetime,
        }
        return Response(visit_data, status=status.HTTP_201_CREATED)