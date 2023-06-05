
from rest_framework import generics

from cargos.models import Cargo
from cargos.serializers import CargoSerializer, CargosSerializer, CargoUpdateSerializer


class CargoListView(generics.ListAPIView):
    serializer_class = CargosSerializer
    queryset = Cargo.objects.all()



class CargoCreateAPIView(generics.CreateAPIView):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()


class CargoDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()


class CargoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CargoUpdateSerializer
    queryset = Cargo.objects.all()


class CargoRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()
