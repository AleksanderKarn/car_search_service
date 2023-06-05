from rest_framework import generics

from cars.models import Car
from cars.serializers import CarSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
